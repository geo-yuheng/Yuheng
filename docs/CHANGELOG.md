# CHANGELOG

变更日志

---

## [1.2.0](https://github.com/geo-yuheng/Yuheng/compare/1.1.0...1.2.0)

主要更新：

+ 在Yuheng自带的`query`中确定只会提供基础的基于字符串模板替换的OverpassQL查询生成，而在`overpass`插件中尝试实现生成和解析非特定格式的OverpassQL。（WIP）
+ 设计了暂定为`GanyuQL`的查询语言的语法
+ 重写了网络读写数据驱动中`network_read()`和`read_network_area()`、`read_network_element()`等方法，并确定`worker应当在数据驱动中执行。

其他更新：

+ 修正了一部分未能更改为`Yuheng`的`Keqing`
+ 修改了`network`中对于返回不同endpoint的判断逻辑和数据储存结构
+ 修改了`Bounds`序列化与反序列化的格式控制
+ 提供了poly文件的数据驱动
+ 一些文档和测试工作

## [1.1.0](https://github.com/geo-yuheng/Yuheng/compare/1.0.2...1.1.0)

相比于上一版本，这一版本更新的内容主要有：

+ 包名更改
+ 大量文档工作和文档构建流水线
+ 修正了部分测试用例未能导入的问题

## [1.0.2](https://github.com/geo-yuheng/Yuheng/compare/1.0.1...1.0.2)

相比于1.0.1，这一版本更新的内容主要有：

+ 将`parse_url`和`nominatim`相关代码均拆分出基础功能作为plugin，而`parse_xml`作为builtin method保留
+ 修复了`Member`中poka-yoke失效的问题，现在构造`Member`对象时可自由选用`ref`或者`id`作为attribute
+ 改善了测试用例的import方法，现在可以无视`/tests`不能跨top-level引入`/src`内开发中代码的问题了，方便即时测试
+ 添加了完全依靠构造器创建对象并添加到`Waifu`对象中的方法
+ 以注释的形式对未来可能的改进方向添加TODO