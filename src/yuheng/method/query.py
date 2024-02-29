# query生成了以后，query模块并不负责执行，只是把QL返回给需要QL的上层函数
# 调用query模块的上层函数一般是从network read driver在指定overpass作为来源后，希望生成一个QL
# 在它获取QL后，也不会要求network模块提供conductor来执行，它自己就是执行网络请求（底层requests/httpx）的模块
# 后话：它读取了以后会送去parse
from typing import List


def overpass_query(query_content: str) -> None:
    print("NOTE: currently only support basic ql")
    # from src.yuheng.plugin.overpass.overpass_parse import remove_comment
    # # 默认不调用overpass插件的方法，因为这就和lxml与regex一样，默认的xml和re也不是不能用，只是如果基本的检测能跑就行了，组合一下类型，只用yuheng默认的方法
    # lines = (
    #     remove_comment(
    #         query_content,
    #     )
    #     .replace("\n", "")  # 解析时是否按单行解析应设置为单独的参数，因为和parse分离了，要如何传参是个大问题。
    #     .replace("(", "")
    #     .replace(")", "")
    #     .split(";")
    # )
    lines = query_content
    types = ["node", "way", "relation"] + ["nw", "nr", "wr", "nwr"]
    operations = set()
    for line in lines:
        for type in types:
            if type in line:
                operations = operations.union(set([line]))
    print(operations)
    # for operation in operations:
    #     # type:list=operation.jianceleixing
    #     # actions:list=operation.fenliqitayaosu
    #     # temp:Carto=Carto()
    #     # for i in actions:
    #     #     # i就是[k=v]
    #     #     temp=query_in_type(type,query_content)
    #     # 最后剩下的就是逐层查询完了以后的，可以是空
    #     pass # 分离出逐次查询


def ganyu_query(query_content: str) -> None:
    pass


def query(query_content: str, query_language="oVerPass") -> None:
    name_list_overpass: List[str] = [
        name.lower()
        for name in [
            "Overpass",
            "OverpassQuery",
            "OverpassQL",
            "OverpassAPI",
            "OverpassTurbo",
        ]
    ]
    name_list_ganyu: List[str] = [name.lower() for name in ["Ganyu", "Yeyang"]]
    if query_language.lower() in name_list_overpass:
        overpass_query(query_content)
    if query_language.lower() in name_list_ganyu:
        ganyu_query(query_content)
