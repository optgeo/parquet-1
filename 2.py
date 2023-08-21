import geopandas
import json

EXTENT_PATH = '14321.parquet'
GEOJSONS_PATH = '1.geojsons'

extent = geopandas.read_parquet(EXTENT_PATH)

with open(GEOJSONS_PATH, 'r') as f:
  for line in f:
    f = json.loads(line)
    ff = geopandas.GeoDataFrame.from_features([f], 'EPSG:6668')
    clipped = geopandas.clip(ff, extent)
    if not clipped.empty:
      cf = json.loads(clipped.to_json())
      for c in cf['features']:
        f['geometry'] = c['geometry']
        print(json.dumps(f, ensure_ascii=False))
