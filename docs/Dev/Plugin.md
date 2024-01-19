# Plugin

## Official

### `overpass`

Conduct overpass query, can be replaced by other python-overpass library:

+ https://github.com/mvexel/overpass-api-python-wrapper
+ https://github.com/mocnik-science/osm-python-tools
+ https://github.com/DinoTools/python-overpy

Detailed usage still in progress.

### `driver_geojson`

基于 `geojson` 库，并未完全自行实现读取

* 仓库地址：https://github.com/jazzband/geojson
* 包地址：https://pypi.org/project/geojson/
* 文档地址：https://python-geojson.readthedocs.io/en/latest/#

### `driver_topojson`

基于 `topojson` 库，并未完全自行实现读取

* 仓库地址：https://github.com/mattijn/topojson
* 包地址：https://pypi.org/project/topojson/
* 文档地址：https://mattijn.github.io/topojson/

### `driver_poly`

自行实现，提供多种输出方式

可以直接粗转换为Overpass或者其他常见的序列，也可转换为Yuheng的Carto对象或者从Carto对象生成多种序列

## Registry

See: https://github.com/LaoshuBaby/yuheng-plugin-registry