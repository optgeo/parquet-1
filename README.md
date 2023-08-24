# parquet-1
Project Mosaic: GeoParquet test 1

# Demo
## optbv samukawa only with style
https://smb.optgeo.org/ipfs/QmatcFj6wfMdjp6Xg42jQdsQi1JjTekXvCf3ppamaLVTqN

## optbv from GSI, Samukawa only.
https://protomaps.github.io/PMTiles/?url=https%3A%2F%2Fsmb.optgeo.org%2Fipfs%2FQmSPNa7eYAVBMsQPAFx6aMzCrc7xE3fqky7Pgb9CfJaaSg#map=12.48/35.37715/139.38312

## The GeoParquet resource
https://optgeo.github.io/parquet-1/N03-19_14_190101.parquet

## Python code
### install
```sh
pip install geopandas pyarrow fsspec requests aiohttp
```

### demo
```python
import geopandas
import fsspec

url = 'https://optgeo.github.io/parquet-1/N03-19_14_190101.parquet'
with fsspec.open(url) as file:
    df = geopandas.read_parquet(file)

samukawa = df[df['N03_007'] == '14321']
print(samukawa.to_json())
```

# Concept 
Source: https://github.com/UNopenGIS/7/issues/229

## 理念
国連スマート地図グループは、スマート地図バザールを通じて、地理空間情報を際限なく取り込む技法を手に入れました。この技法が我々のホスティング能力を無尽蔵に支えてくれることを前提として、私たちは Smart Maps はこうあるべきという「小さい地図」に取り組むことを決意しました。その実践の道が Project Mosaic です。

Project Mosaic は次の世界観を実世界にもたらすことを目指して具体的な技法の整備を進めます。

1. ウェブ地図は read-only ではなく、自由に読み書きができること。
2. 上記1を通じて、ウェブ地図はユーザに合わせて動的に、多様な姿をとって近づくこと。我々は靴に合わせる足を求めるのではなく、足に合わせる靴を求めます。

これらの技法の適用を通じて、我々はウェブ地図を軽量化し、効率的に使いやすい地図を提供します。

小さい地図は、多くの利点を持っています。軽量なデータはいかなるホスティング環境においてもフットプリントが小さく、ウェブ上でスムーズに動作し、ユーザーの体験を向上させます。また、使いやすいインターフェースを提供することで、地図を活用する際の利便性を高めることができます。

我々は全世界の地図を持ち歩くことができる。しかし、我々は必要な地図を必要なときに必要な形で呼び出すことができる。それが Project Mosaic が目指すユーザ向けアウトカムになると思います。

## 実践
1. 行政界をGeoParquetに変換: 地理空間情報の行政界データをGeoParquet形式に変換し、ウェブのリソースにします。
1. GeoPandasでGeoParquetから行政界データを読み込みます。これにより、手元のフットプリントは小さいまま、必要な場所の行政界の範囲を把握することができます。
1. mercantileとsupermercadoというツールを活用して、ウェブから必要な部分のタイルを取り出します。これにより、地図の範囲を最適化し、必要なデータだけを効率的に取り込みます。
1. tippecanoe-decode と tippecanoe、go-pmtiles を使用して、カスタムの PMTiles を作ります。このとき、地理空間情報の再最適化や融合、圧縮等を行い、軽量で効率的でユーザの用途に合致したスマートタイルを作成します。
1. charitesというツールを使用して、作成したスマートタイルに最適なスタイルと機能を与えます、地図の機能を拡張し、使いやすいスマート地図を完成させます。
1. IPFSでパブリッシュしキャッシュする: 完成したスマート地図をIPFS（InterPlanetary File System）を使って公開し、分散型のデータ共有を実現します。IPFSにより、地図データを効率的に配信し、キャッシュすることが可能になります。

以上の技術的な手順により、mosaic projectでは、行政界データを取り込み、必要な領域のタイルをスマートタイルとして再生成し、IPFSを使って公開し、ユーザーにより効率的で使いやすい地図を提供することを目指しています。分散ウェブの効果によって経済性と安全性が強化される見込みがあることも魅力です。

国連スマート地図グループは、Project Mosaic という実践を進捗させることより、より多くの人々が地理空間情報を活用できる環境を創り上げます。

## 当座の作業のメモ
作業を次のフェーズに分離する

1. 地方公共団体のポリゴンと、そのポリゴンに掛かり得るベクトルデータとを得るフェーズ。
2. 

## About social preview image
Room from a hotel in the Cours d'Albret, Bordeaux: https://www.metmuseum.org/art/collection/search/199390
