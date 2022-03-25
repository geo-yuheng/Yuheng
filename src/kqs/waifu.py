from typing import Dict, List
from xml.dom import minidom
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

from .model import BaseOsmModel, Bounds, Member
from .type import Node, Relation, Way
from .global_const import KQS_GENERATOR, KQS_START_ID, KQS_VERSION


class Waifu:
    def __init__(self):
        self.node_dict: Dict[int, Node] = {}
        self.bounds_list: List[Bounds] = []
        self.version: str = "0.6"
        self.way_dict: Dict[int, Way] = {}
        self.generator: str = KQS_GENERATOR + "/" + KQS_VERSION
        self.relation_dict: Dict[int, Relation] = {}

    @staticmethod
    def __set_attrib(attrib: Dict[str, str], key: str, value):
        if value is not None:
            attrib[key] = str(value)

    def __parse_node(self, element: Element):
        attrib: Dict[str, str] = element.attrib
        tag_dict: Dict[str, str] = {}
        for sub_element in element:
            tag_dict[sub_element.attrib["k"]] = sub_element.attrib["v"]
        self.node_dict[int(attrib["id"])] = Node(attrib, tag_dict)

    def __parse_way(self, element: Element):
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
        self.way_dict[int(attrib["id"])] = Way(attrib, tag_dict, nd_list)

    def __parse_relation(self, element: Element):
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
        self.relation_dict[int(attrib["id"])] = Relation(
            attrib, tag_dict, member_list
        )

    def read_file(self, file_path: str):
        tree: ElementTree = ET.parse(file_path)
        root: Element = tree.getroot()
        for element in root:
            if element.tag == "node":
                self.__parse_node(element)
            elif element.tag == "way":
                self.__parse_way(element)
            elif element.tag == "relation":
                self.__parse_relation(element)
            elif element.tag == "bounds":
                self.bounds_list.append(Bounds(element.attrib))
            else:
                # raise TypeError('Unexpected element tag type: ' + element.tag)
                pass

    def read_memory(self, text: str):
        root: Element = ET.fromstring(text)
        for element in root:
            if element.tag == "node":
                self.__parse_node(element)
            elif element.tag == "way":
                self.__parse_way(element)
            elif element.tag == "relation":
                self.__parse_relation(element)
            elif element.tag == "bounds":
                self.bounds_list.append(Bounds(element.attrib))
            else:
                # raise TypeError('Unexpected element tag type: ' + element.tag)
                pass

    # def read_network():
    # https://github.com/enzet/map-machine/blob/main/map_machine/osm/osm_getter.py

    def write(self, file_path: str):
        root: Element = Element("osm")
        root.attrib["version"] = self.version
        root.attrib["generator"] = self.generator

        for i in self.bounds_list:
            element: Element = Element("bounds")
            Waifu.__set_attrib(element.attrib, "minlat", i.min_lat)
            Waifu.__set_attrib(element.attrib, "minlon", i.min_lon)
            Waifu.__set_attrib(element.attrib, "maxlat", i.max_lat)
            Waifu.__set_attrib(element.attrib, "maxlon", i.max_lon)
            Waifu.__set_attrib(element.attrib, "origin", i.origin)
            root.append(element)

        def base_osm_model_to_xml(
            tag_name: str, model: BaseOsmModel
        ) -> Element:
            tag: Element = Element(tag_name)
            tag.attrib["id"] = str(model.id)
            Waifu.__set_attrib(tag.attrib, "action", model.action)
            Waifu.__set_attrib(tag.attrib, "timestamp", model.timestamp)
            Waifu.__set_attrib(tag.attrib, "uid", model.uid)
            Waifu.__set_attrib(tag.attrib, "user", model.user)
            tag.attrib["visible"] = "true" if model.visible else "false"
            Waifu.__set_attrib(tag.attrib, "version", model.version)
            Waifu.__set_attrib(tag.attrib, "changeset", model.changeset)
            for k, v in model.tags.items():
                sub_element: Element = Element("tag")
                sub_element.attrib["k"] = k
                sub_element.attrib["v"] = v
                tag.append(sub_element)
            return tag

        for i in self.node_dict.values():
            node: Element = base_osm_model_to_xml("node", i)
            node.attrib["lat"] = str(i.lat)
            node.attrib["lon"] = str(i.lon)
            root.append(node)
        for i in self.way_dict.values():
            way: Element = base_osm_model_to_xml("way", i)
            for ref in i.nds:
                e: Element = Element("nd")
                e.attrib["ref"] = str(ref)
                way.append(e)
            root.append(way)
        for i in self.relation_dict.values():
            relation = base_osm_model_to_xml("relation", i)
            for member in i.members:
                e: Element = Element("member")
                e.attrib["type"] = member.type
                e.attrib["ref"] = str(member.ref)
                e.attrib["role"] = member.role
                relation.append(e)
            root.append(relation)

        raw_text = ET.tostring(root)
        dom = minidom.parseString(raw_text)
        with open(file_path, "w", encoding="utf-8") as file:
            dom.writexml(file, indent="\t", newl="\n", encoding="utf-8")

    def __new_id(self, model_dict: Dict[int, BaseOsmModel]) -> int:
        """
        生成未使用过的新id。如果已经有新要素，则取id最小的要素并减1，没有则取KQS_START_ID。
        :param model_dict:结点、路径、关系数据字典。
        :return: id
        """
        min_id: int = min(model_dict.keys())
        min_id = min_id if min_id < 0 else KQS_START_ID
        return min_id - 1

    def new_node_id(self) -> int:
        """
        生成未使用过的新结点id。
        :return: 结点id
        """
        return self.__new_id(self.node_dict)

    def new_way_id(self) -> int:
        """
        生成未使用过的新路径id。
        :return: 路径id
        """
        return self.__new_id(self.way_dict)

    def new_relation_id(self) -> int:
        """
        生成未使用过的新关系id。
        :return: 关系id
        """
        return self.__new_id(self.relation_dict)