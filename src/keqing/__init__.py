import time
from typing import Dict, List
from xml.dom import minidom
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

from .basic.global_const import (
    KEQING_CORE_NAME,
    KEQING_START_ID,
    KEQING_VERSION,
)
from .basic.model import BaseOsmModel
from .method.network import get_headers, get_server
from .method.parse_xml import (
    parse_node,
    parse_relation,
    parse_way,
    pre_parse_classify,
)
from .method.transform import prefix_abbreviation
from .type.constraint import Bounds, Member
from .type.element import Node, Relation, Way


class Waifu:
    def __init__(self):
        self.node_dict: Dict[int, Node] = {}
        self.bounds_list: List[Bounds] = []
        self.version: str = "0.6"
        self.way_dict: Dict[int, Way] = {}
        self.generator: str = (
            KEQING_CORE_NAME.replace("_Sword", "") + "/" + KEQING_VERSION
        )
        self.relation_dict: Dict[int, Relation] = {}

    @staticmethod
    def __set_attrib(attrib: Dict[str, str], key: str, value):
        if value is not None:
            attrib[key] = str(value)

    def meow(self):
        import logging
        # from loguru import logger

        logging.basicConfig(level=logging.INFO)
        logging.info(
            str(
                "\n"
                + "==============================\n"
                + "Keqing load successful!\n"
                + "==============================\n"
                + (
                    "node    : "
                    + str(len(self.node_dict))
                    + "\n"
                    + "way     : "
                    + str(len(self.way_dict))
                    + "\n"
                    + "relation: "
                    + str(len(self.relation_dict))
                    + "\n"
                    + "bounds  : "
                    + str(len(self.bounds_list))
                    + "\n"
                )
                + "=============================="
            )
        )

    def read(
        self,
        mode=None,
        file_path="",
        text="",
        url="",
        fpath="",
        data_driver="",
    ):
        def pre_read_warn(mode: str, file_path: str, text: str, url: str):
            if url != "" and (mode != "network" and mode != "n"):
                if ("http://" in url) or ("https://" in url):
                    print(
                        "WARN:You may intent to request from network, but you enter another mode."
                    )
            if mode == "text" or mode == "t":
                print(
                    'WARN:"text" is not standard Keqing read mode, it caughted by fallback system and recognized as "memory"'
                )

        time_start = time.time()
        if file_path == "" and fpath != "":
            file_path = fpath

        if (mode == "file" or mode == "f") or (
            (mode == "memory" or mode == "m" or mode == "text" or mode == "t")
            and text == ""
        ):
            pre_read_warn(mode=mode, file_path=file_path, text=text, url=url)
            if file_path != "" and text != "":
                print(
                    "WARN:You add parameter for both file mode and memory mode! Keqing will choose you designated **file** mode"
                )
            self.read_file(file_path)
        elif (
            mode == "memory" or mode == "m" or mode == "text" or mode == "t"
        ) or ((mode == "file" or mode == "f") and file_path == ""):
            pre_read_warn(mode=mode, file_path=file_path, text=text, url=url)
            if file_path != "" and text != "":
                print(
                    "WARN:You add parameter for both file mode and memory mode! Keqing will choose you designated **memory** mode"
                )
            self.read_memory(text)
        elif mode == "network" or mode == "n":
            # pre_read_warn(mode=mode,file_path=file_path,text=text,url=url) # No need, we may need warn a 'mode="network" + url=""' situation.
            self.read_memory(url)
        else:
            raise TypeError(f"Unexpected read mode: {mode}")

        time_end = time.time()
        print("[TIME]: " + str(round((time_end - time_start), 3)) + "s" + "\n")
        self.meow()

    def read_file(self, file_path: str):
        tree: ElementTree = ET.parse(file_path)
        root: Element = tree.getroot()
        pre_parse_classify(
            self.node_dict,
            self.way_dict,
            self.relation_dict,
            self.bounds_list,
            root,
        )

    def read_memory(self, text: str):
        root: Element = ET.fromstring(text)
        pre_parse_classify(
            self.node_dict,
            self.way_dict,
            self.relation_dict,
            self.bounds_list,
            root,
        )

    def read_network(self, mode="api", server="OSM", quantity="", **kwargs):
        # version problem haven't been introduced
        if quantity != "":
            if quantity == "area":
                # parse SWNE
                self.read_network_area()
            else:
                if kwargs.get("element_id"):
                    self.read_network_element(
                        element_id=kwargs["element_id"],
                        type=kwargs.get("type"),
                        server=server,
                    )
                else:
                    # parse Element
                    pass
        else:
            if kwargs.get("url"):
                # download directly, then judge
                pass
            else:
                return None
        pass

    def read_network_area(self, S, W, N, E, mode="api", server="OSM"):
        if mode == "api":
            # https://github.com/enzet/map-machine/blob/main/map_machine/osm/osm_getter.py
            # need to add server change function
            pass
        if mode == "overpass":
            pass
        pass

    def read_network_element(
        self, element_id: str, type="undefined", mode="api", server="OSM"
    ):
        def have_multi_elements(element_id) -> bool:
            if "," in element_id:
                # have comma or space between multi element
                return True

        if have_multi_elements(element_id):
            self.read_network_element_batch(element_id)
        else:
            if (
                (type == "node" or type == "n")
                or (type == "way" or type == "w")
                or (type == "relation" or type == "r")
            ):
                import requests

                pure_id = (
                    element_id.replace("n", "")
                    .replace("w", "")
                    .replace("r", "")
                )
                if "v" in pure_id:
                    version = pure_id.split("v")[1]
                    pure_id = pure_id.split("v")[0]
                url = (
                    get_server(server)
                    + prefix_abbreviation(type, mode="p2prefix")
                    + "/"
                    + pure_id
                )
                headers = get_headers()
                print("url:", url)
                print("headers:", headers)
                response = requests.get(url=url, headers=headers).text
                print(response)
                self.read_memory(response)
            else:
                # detect type single request
                # warn that if parameter type and element_id implied type don't match
                pass

    def read_network_element_batch(
        self, element_id=None, mode="api", server="OSM"
    ):
        # it can be string or list
        # https://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:_GET_/api/0.6/[nodes|ways|relations]?#parameters
        pass

    def write(self, mode=None, file_path="", data_driver=""):
        def is_limit_valid(ignore=False):
            # conduct limit check
            # for ele in nwr
            # if ele.is_limit_valid=True
            return True

        if mode == "file":
            self.write_file(file_path)
        elif mode == "network":
            self.write_network()
        elif mode == "josm_remote_control":
            # maybe remote_control_josm will be better?
            self.write_josm_remote_control()
        else:
            raise TypeError(f"Unexpected write mode: {mode}")

    def write_file(self, file_path: str, only_diff=False):
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
            if i.has_diff() and i.action != "delete":
                i.action = "modify"
            node: Element = base_osm_model_to_xml("node", i)
            node.attrib["lat"] = str(i.lat)
            node.attrib["lon"] = str(i.lon)
            root.append(node)
        for i in self.way_dict.values():
            if i.has_diff() and i.action != "delete":
                i.action = "modify"
            way: Element = base_osm_model_to_xml("way", i)
            for ref in i.nds:
                e: Element = Element("nd")
                e.attrib["ref"] = str(ref)
                way.append(e)
            root.append(way)
        for i in self.relation_dict.values():
            if i.has_diff() and i.action != "delete":
                i.action = "modify"
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

    def write_network(self):
        # will imply in the future
        pass

    def write_josm_remote_control(self):
        # Thanks to @AustinZhu's idea about this branch of output stream
        # will imply in the long future
        pass

    def __new_id(self, model_dict: Dict[int, BaseOsmModel]) -> int:
        """
        生成未使用过的新id。如果已经有新要素，则取id最小的要素并减1，没有则取KQS_START_ID。
        :param model_dict:结点、路径、关系数据字典。
        :return: id
        """
        min_id: int = min(model_dict.keys())
        min_id = min_id if min_id < 0 else int(KEQING_START_ID)
        return min_id - 1

    def flush(self, id: str) -> None:
        # 传入形如"n123,w456,r789"的字符串，并批量执行flush
        pass

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
