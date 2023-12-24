from yuheng.basic.model import Base

# 也应该提供pandas的df转换，内建的，比如提供一个export_as_df，调用就创建对象里一个成员，不调用不创建。这个成员是一个df。需要import但是不用就不会import不会报错。没装别掉用。

# 固定id/lat、lon等几列，至于namezh/type/operator之类要不要展开若干栏还是所有tag打json合在tags一栏，建议智能自适应。所有数据中超过50的element/tagged element具有的key自动展开为列。（tags里面删不删另说）这样便于结构化或者关系化的整批提取指定字段并使用它筛选，直接df[name]==建筑然后对子df做[id] 确实会比以前层层查询快，要允许这个需求，不然学姐为啥要我交付id，latlon的csv啊。pandas强行回到结构化和keqing目前的全对象化都有特色。不过我们肯定不要和pgsql竞争。

# 随想

class OSM(Base):
    def __init__(self) -> None:
        super().__init__()


class OSH(Base):
    def __init__(self) -> None:
        super().__init__()


class OSC(Base):
    def __init__(self) -> None:
        super().__init__()

    def Modify():
        pass

    def Create():
        # Call create function to create them in memory
        pass

    def Delete():
        # If element already in memory, delete it. (And save other unfound id)
        pass
