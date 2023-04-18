from typing import Dict, List
from xml.etree.ElementTree import Element

from src.keqing.type.constraint import Bounds, Member
from src.keqing.type.element import Node, Relation, Way


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


def parse_node(node_dict, element: Element):
    attrib: Dict[str, str] = element.attrib
    tag_dict: Dict[str, str] = {}
    for sub_element in element:
        tag_dict[sub_element.attrib["k"]] = sub_element.attrib["v"]
    node_dict[int(attrib["id"])] = Node(attrib, tag_dict)


def parse_way(way_dict, element: Element):
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
    relation_dict[int(attrib["id"])] = Relation(attrib, tag_dict, member_list)
