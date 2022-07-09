# Tests

## Tests-list

### 内部测试用例

1. test_load

这组测试用例用于检查Keqing能否正常加载来自不同来源的osm、osh、osc文件。

They are all real data export by OSM Website or other well-known OSM editor, such as JOSM, level0. iD/RapiD 's exported `.osc` file will be supported soon.

为实现交叉验证，提供不通过Keqing的方法来验证数目。用功能无错误的文本编辑器或IDE搜索`<bound`, `<node`, `<way`, `<relation`并分别计数，作为对应元素的数量，看Keqing是否能正常加载。

NOTE！测试用例目录未来可能会重置，届时请注意调整目录结构！

2. test_iterator

这组测试用例用于检查循环器是否能正常迭代。通常在满足第一组测试用例的情况下是可以的。

3. test_select

这组测试用例用于检查根据查询语句能否查询到正确的结果。

### 外部测试用例

1. osmcode/osm-testdata

https://github.com/osmcode/osm-testdata/tree/master/xml/data