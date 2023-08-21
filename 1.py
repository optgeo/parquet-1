import geopandas
import fsspec
import subprocess
import json
import re

MIN_ZOOM = 4
MAX_ZOOM = 16
TEMPLATE_URL = 'https://maps.gsi.go.jp/xyz/optimal_bvmap-v1/{z}/{x}/{y}.pbf'
EXTENTS_URL = 'https://optgeo.github.io/parquet-1/N03-19_14_190101.parquet'
ATTRIBUTE_NAME_FOR_CITY = 'N03_007'

def get_extent(url, city):
  with fsspec.open(url) as file:
    df = geopandas.read_parquet(file)
  return df[df[ATTRIBUTE_NAME_FOR_CITY] == city]

def generate_tiles(extent, z): 
  command = ['supermercado', 'burn', str(z)] 
  process = subprocess.run(command, input=extent.to_json(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  for l in process.stdout.splitlines():
    x, y, z = json.loads(l)
    yield [z, x, y]

def get_cmd(template, zxy):
  url = re.sub("{z}", str(zxy[0]), template)
  url = re.sub("{x}", str(zxy[1]), url)
  url = re.sub("{y}", str(zxy[2]), url)
  return "curl -o {}-{}-{}.pbf {}; tippecanoe-decode -c {}-{}-{}.pbf {} {} {}; rm {}-{}-{}.pbf".format(
    zxy[0], zxy[1], zxy[2], url, zxy[0], zxy[1], zxy[2], zxy[0], zxy[1], zxy[2], zxy[0], zxy[1], zxy[2]
  )

def generate_cmds(extent):
  for z in range(MIN_ZOOM, MAX_ZOOM + 1):
    for zxy in generate_tiles(extent, z):
      yield get_cmd(TEMPLATE_URL, zxy)

extent = get_extent(EXTENTS_URL, '14321') #14321
extent.to_parquet('14321.parquet')
for cmd in generate_cmds(extent):
  print(cmd)
