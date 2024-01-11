# CHANGELOG

变更日志

---

## 1.2.0

主要更新：

+ 在Yuheng自带的query中确定只会提供基础的基于字符串模板替换的overpass查询生成，而在overpass插件中尝试实现生成和解析非特定格式的OverpassQL。（WIP）
+ 设计了暂定为GanyuQL的查询语言的语法
+ 重写了网络读写数据驱动中network_read()和read_network_area()、read_network_element()等方法，并确定worker应当在数据驱动中执行。

其他更新：

+ 修正了一部分未能更改为Yuheng的Keqing
+ 修改了network中对于返回不同endpoint的判断逻辑和数据储存结构
+ 修改了Bounds序列化与反序列化的格式控制
+ 提供了poly文件的数据驱动
+ 一些文档和测试工作

## [1.0.2](https://github.com/LaoshuBaby/Yuheng/compare/1.0.1...1.0.2)

相比于1.0.1，这一版本更新的内容主要有：

+ 将parse_url和nominatim相关代码均拆分出基础功能作为plugin，而parse_xml作为builtin method保留
+ 修复了Member中poka-yoke失效的问题，现在构造Member对象时可自由选用ref或者id作为attribute
+ 改善了测试用例的import方法，现在可以无视/tests不能跨top-level引入/src内开发中代码的问题了，方便即时测试
+ 添加了完全依靠构造器创建对象并添加到Waifu对象中的方法
+ 以注释的形式对未来可能的改进方向添加TODO