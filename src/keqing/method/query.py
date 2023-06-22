def remove_comment(query_content: str) -> str:
    # priority: block comment > line comment
    # block comment
    # suggestion: regex
    # line comment
    query_content = query_content.split("\n")
    query_content_judge = [line.replace(" ", "") for line in query_content]
    query_content_none_comment = []
    for i in range(len(query_content_judge)):
        if i[:2] != "//":
            query_content_none_comment.append(line)
    query_content = "".join(query_content)
    # warning: if a line not begin with comment, it't comment won't be removed, I still waiting for a good method.
    pass
    return query_content


# def query_in_type(type: list, query_content: str) -> Waifu:
#     return Waifu()
# 不能直接返回Waifu，因为并不打算撤销这套__init__里放单独一个waifu的结构。这里只能返回其他内容（如xml/json）再在waifu里面parse它


def overpass_query(query_content: str) -> None:
    print("NOTE: currently only support basic ql")
    lines = (
        remove_comment(query_content)
        .replace("\n", "")
        .replace("(", "")
        .replace(")", "")
        .split(";")
    )
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
    #     # temp:Waifu=Waifu()
    #     # for i in actions:
    #     #     # i就是[k=v]
    #     #     temp=query_in_type(type,query_content)
    #     # 最后剩下的就是逐层查询完了以后的，可以是空
    #     pass # 分离出逐次查询


def ganyu_query(query_content: str) -> None:
    pass


def query(query_content: str, query_language: str) -> None:
    query_language = "Overpass"
    name_list_overpass = [
        "Overpass",
        "OverpassQuery",
        "OverpassQL",
        "OverpassAPI",
        "OverpassTurbo",
    ]
    name_list_ganyu = ["Ganyu", "Yeyang"]
    if query_language in name_list_overpass:
        overpass_query(query_content)
    if query_language in name_list_ganyu:
        ganyu_query(query_content)


query(
    open("../../../tests/overpassql/telecommunication.overpassql"), "Overpass"
)
