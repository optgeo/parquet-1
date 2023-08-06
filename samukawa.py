import geopandas
import fsspec

url = 'https://optgeo.github.io/parquet-1/N03-19_14_190101.parquet'
with fsspec.open(url) as file:
    df = geopandas.read_parquet(file)

samukawa = df[df['N03_007'] == '14321']
print(samukawa.to_json())
