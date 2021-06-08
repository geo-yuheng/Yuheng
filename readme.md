# OSM编辑工具

一些批量编辑OSM数据的工具。

彻底重写原来的屎山，目前只实现了osm文件的读写，在某人强烈安利下先建个仓库_(:з」∠)_

## PyOsm

osm数据对象。

```python
from keqing_my_waifu.pyosm import PyOsm

# 实例化PyOsm对象并从osm文件读取
osm = PyOsm()
osm.from_file('./tmp.osm')
# 打印所有路径的名称
for way in osm.way_dict.values():
    if 'name' in way.tags:
        print(way.tags['name'])
# 写入到osm文件
osm.write('./test.osm')
```
