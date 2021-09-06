# OSM编辑工具

一些批量编辑OSM数据的工具。

彻底重写原来的屎山，目前只实现了osm文件的读写，在某人强烈安利下先建个仓库_(:з」∠)_

## PyOsm

osm数据对象。

### 使用示例

把有name但没有name:zh标签的点，设置name:zh为name的值。

```python
from keqing_my_waifu.pyosm import PyOsm

# 从.osm文件加载PyOsm对象
pyosm = PyOsm()
pyosm.from_file('./demo.osm')

# 遍历所有点
for node in pyosm.node_dict.values():
    # 跳过无name或有name:zh标签的点
    if 'name' not in node.tags or 'name:zh' in node.tags:
        continue

    # 获取name，并设置name:zh
    name = node.tags['name']
    node.tags['name:zh'] = name

    # 如果修改前后的标签有差异，则打印差异，并标记为已修改
    if node.has_diff():
        node.print_diff()
        node.action = 'modify'

# 写到.osm文件
pyosm.write('../demo_changed.osm')
```
