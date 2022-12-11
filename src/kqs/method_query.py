def overpass_query(query_content: str) -> None:
    print("NOTE: currently only support basic ql")
    lines = (
        query_content.replace("\n", "")
        .replace("(", "")
        .replace(")", "")
        .split(";")
    )
    types = ["node", "way", "relation"] + ["nw", "nr", "wr", "nwr"]
    operations = set()
    for line in lines:
        for type in types:
            if type in line:
                operations=operations.union(set([line]))
    print(operations)


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

