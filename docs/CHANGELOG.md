# CHANGELOG

变更日志

---

## 1.0.2

相比于1.0.1，这一版本更新的内容主要有：

+ 将parse_url和nominatim相关代码均拆分出基础功能作为plugin，而parse_xml作为builtin method保留
+ 修复了Member中poka-yoke失效的问题，现在构造Member对象时可自由选用ref或者id作为attribute
+ 改善了测试用例的import方法，现在可以无视/tests不能跨top-level引入/src内开发中代码的问题了，方便即时测试
+ 添加了完全依靠构造器创建对象并添加到Waifu对象中的方法
+ 以注释的形式对未来可能的改进方向添加TODO