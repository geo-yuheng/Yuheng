from typing import Dict, List
from xml.etree.ElementTree import Element


from keqing.type.constraint import Member, Bounds
from keqing.type.element import Node, Way, Relation


def parse_node(node_dict, element: Element):
    # Will move to parse.py
    attrib: Dict[str, str] = element.attrib
    tag_dict: Dict[str, str] = {}
    for sub_element in element:
        tag_dict[sub_element.attrib["k"]] = sub_element.attrib["v"]
    node_dict[int(attrib["id"])] = Node(attrib, tag_dict)


def parse_way(way_dict, element: Element):
    # Will move to parse.py
    attrib: Dict[str, str] = element.attrib
    tag_dict: Dict[str, str] = {}
    nd_list: List[int] = []

    for sub_element in element:
        if sub_element.tag == "nd":
            nd_list.append(int(sub_element.attrib["ref"]))
        elif sub_element.tag == "tag":
            tag_dict[sub_element.attrib["k"]] = sub_element.attrib["v"]
        else:
            raise TypeError(
                f"Unexpected element tag type: {sub_element.tag} in Way"
            )
    way_dict[int(attrib["id"])] = Way(attrib, tag_dict, nd_list)


def parse_relation(relation_dict, element: Element):
    # Will move to parse.py
    attrib: Dict[str, str] = element.attrib
    tag_dict: Dict[str, str] = {}
    member_list: List[Member] = []

    for sub_element in element:
        if sub_element.tag == "member":
            member_list.append(
                Member(
                    sub_element.attrib["type"],
                    int(sub_element.attrib["ref"]),
                    sub_element.attrib["role"],
                )
            )
        elif sub_element.tag == "tag":
            tag_dict[sub_element.attrib["k"]] = sub_element.attrib["v"]
        else:
            raise TypeError(
                f"Unexpected element tag type: {sub_element.tag} in Relation"
            )
    relation_dict[int(attrib["id"])] = Relation(
        attrib, tag_dict, member_list
    )


def parse(element: Element):
    # judge whether is N/W/R then invoke function.
    pass


def pre_parse_classify(node_dict, way_dict, relation_dict, bounds_list, root):
    for element in root:
        if element.tag == "node":
            parse_node(node_dict, element)
        elif element.tag == "way":
            parse_way(way_dict, element)
        elif element.tag == "relation":
            parse_relation(relation_dict, element)
        elif element.tag == "bounds":
            bounds_list.append(Bounds(element.attrib))
        else:
            # raise TypeError('Unexpected element tag type: ' + element.tag)
            pass

# Waiting
def t2type(t: str) -> str:
    if t == "n" or t == "node":
        return "node"
    if t == "w" or t == "way":
        return "way"
    if t == "r" or t == "relation":
        return "relation"
    if t == "c" or t == "changeset":
        return "changeset"
    if t == "v" or t == "version":
        return "version"

def url_parse(url:str,domain:str="openstreetmap.org"):
    type:str="node"
    id:int=0
#     import urlib
    url=url.split(domain)
    #test case
    # node/way/relation/changeset
    # openstreetmap.org/node/5739239358
    #　http://www.openstreetmap.org/node/5739239358
    # https://www.openstreetmap.org/node/5739239358#map=19/25.53658/113.53478
    #　https://www.openstreetmap.org/node/5739239358#map=19/25.53658/113.53444&layers=TNDG
    #　https://www.openstreetmap.org/node/5739239358?locale=zh-TW#map=19/25.53658/113.53444
    # https://www.openstreetmap.org/node/5739239358/history#map=19/25.53668/113.53436
    return [type,id]

parse_url_fallback=["osm.org","openstreetmap.org", "openstreetmap.com"]# parse this js file https://github.com/openstreetmap/dns/blob/master/dnsconfig.js
