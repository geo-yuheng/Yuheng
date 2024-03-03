import os
import sys
import time
from typing import Dict, List, Union
from xml.dom import minidom
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

from .basic.global_const import (
    YUHENG_CORE_NAME,
    YUHENG_PATH,
    YUHENG_START_ID,
    YUHENG_VERSION,
    get_yuheng_path,
)
from .basic.log import log
from .basic.model import BaseOsmModel
from .component.type_constraint import Bounds, Member
from .component.type_element import Node, Relation, Way
from .method import query
from .method.network import get_endpoint_api, get_headers
from .method.parse import (
    parse_node,
    parse_relation,
    parse_way,
    pre_parse_classify,
)
from .method.transform import prefix_normalization

log.info("loguru enabled")

class Carto:
    def __init__(self):
        self.version: str = "0.6"
        self.generator: str = (
            YUHENG_CORE_NAME.replace("_Sword", "") + "/" + YUHENG_VERSION
        )
        self.bounds_list: List[Bounds] = []
        self.node_dict: Dict[int, Node] = {}
        self.way_dict: Dict[int, Way] = {}
        self.relation_dict: Dict[int, Relation] = {}

    @staticmethod
    def __set_attrib(attrib: Dict[str, str], key: str, value):
        if value is not None:
            attrib[key] = str(value)

    @staticmethod
    def insert_to_dict(spec_dict, element_list):
        for i in element_list:
            spec_dict[int(i.id)] = i

    def meow(self) -> None:
        log.info(
            "\n"
            + "==============================\n"
            + "Yuheng load successful!\n"
            + "==============================\n"
            + f"node    : {str(len(self.node_dict))}\n"
            + f"way     : {str(len(self.way_dict))}\n"
            + f"relation: {str(len(self.relation_dict))}\n"
            + f"bounds  : {str(len(self.bounds_list))}\n"
            + "=============================="
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
                    log.warning(
                        "You may intent to request from network, but you enter another mode."
                    )
            if mode == "text" or mode == "t":
                log.warning(
                    'You use "text" as "mode" and it isn\'t standard Yuheng read mode, it caughted by fallback system and recognized as "memory"'
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
                log.warning(
                    "You add parameter for both file mode and memory mode! Yuheng will choose you designated **file** mode"
                )
            self.read_file(file_path)
        elif (
            mode == "memory" or mode == "m" or mode == "text" or mode == "t"
        ) or ((mode == "file" or mode == "f") and file_path == ""):
            pre_read_warn(mode=mode, file_path=file_path, text=text, url=url)
            if file_path != "" and text != "":
                log.warning(
                    "You add parameter for both file mode and memory mode! Yuheng will choose you designated **memory** mode"
                )
            self.read_memory(text)
        elif mode == "network" or mode == "n":
            # pre_read_warn(mode=mode,file_path=file_path,text=text,url=url) # No need, we may need warn a 'mode="network" + url=""' situation.
            self.read_memory(url)
        else:
            raise TypeError(f"Unexpected read mode: {mode}")

        time_end = time.time()
        log.info(f"[TIME]: Read cost {str(round((time_end - time_start), 3))}s")
        self.meow()

    def read_file(self, file_path: str):
        try:
            tree: ElementTree = ET.parse(file_path)
            root: Element = tree.getroot()
            pre_parse_classify(
                self.node_dict,
                self.way_dict,
                self.relation_dict,
                self.bounds_list,
                root,
            )
        except FileNotFoundError:
            log.error("文件不存在，请检查文件路径")
        except PermissionError:
            log.error("无权访问文件，请检查文件权限")
        except ET.ParseError:
            log.error("XML 解析失败，请检查文件内容是否为有效的 XML 格式")
        except Exception as e:
            log.error(f"发生未知错误 - {str(e)}")

    def read_memory(self, text: str):
        try:
            root: Element = ET.fromstring(text)
            pre_parse_classify(
                self.node_dict,
                self.way_dict,
                self.relation_dict,
                self.bounds_list,
                root,
            )
        except ET.ParseError:
            log.error("XML 解析失败，请检查文本内容是否为有效的 XML 格式")
        except Exception as e:
            log.error(f"发生未知错误 - {str(e)}")

    def read_network(self, target="", source="api", endpoint="osm", **kwargs):
        """
        所有类型的网络请求最终都将返回一个work_url，在read_network中调用worker来获取work_load，最后转给read_memory读取这个work_load
        无论如何先获取url，才能算hash确定是否使用cache

        mandatory arguments:
        * target：表数量，是想下载单一个元素还是一片区域。建议后续改为target，毕竟数量只有单或者多。区域和batch都是多。target可以为element/area。
        * source： 是从api读还是 overpass读，还是其他网站的野数据（比如IA恰好存了一个xml之类的情况）
        * endpoint：填osm/ogf或者osmru/osmde/kumi之类的

        optional arguments:
        * element_type： 下载元素的时候指定nwr，部分情况下可能冗余。
        * element_id: 下载除了area以外都需要。强制传列表，一个也得列表。出于兼容性，不是列表的字符串会被转换成列表。
        * allow_cache: 将会把请求的各种信息（含url，主要是url）hash以后创建一个cache文件名，如果重复请求的话不需要对代码作出修改就自动用缓存，避免反复打目标机
        * local_overpassql_path：overpass语句不会自动生成而是照抄本地文件内的
        * version： 读取指定版本的文件
        * child: 是否含子成员（int）。0或小于0为不包含。1时，对路径就是所有点，对关系就是所有成员。2时，对路径所有点，关系内路径的点和子关系的成员也下载。child=2时与官方API中的/full等价。3或更大时为无穷尽直到找出所有子子孙孙。
        """

        def get_cache_filename(worl_url: str) -> str:
            import hashlib

            url_hash = hashlib.new(
                name="md5", data=work_url.encode("utf-8")
            ).hexdigest()
            url_safe = (
                work_url.replace("https://", "")
                .replace("http://", "")
                .replace("/", "_")
                .replace("-", "_")
                .replace("#", "_")
                .replace("$", "_")
                .replace("%", "_")
                .replace("&", "_")
                .replace("?", "_")
                .replace(",", "_")
                .replace("=", "_")
                .replace(".", "_")
            )
            return url_safe + "__" + url_hash + ".osm"

        def worker(work_url: str, allow_cache: bool) -> str:
            import requests

            log.info(f"allow_cache={allow_cache}")

            response = requests.get(
                url=work_url,
                headers=get_headers(),
            ).text

            if allow_cache:
                url_cache_filename = get_cache_filename(work_url)

                log.info(f"cache file: {url_cache_filename}")

                with open(
                    os.path.join(
                        get_yuheng_path(), "cache", url_cache_filename
                    ),
                    "w",
                    encoding="utf-8",
                ) as f_cache:
                    f_cache.write(response)

            return response

        def url_of_overpass_quary(ql_content: str, endpoint="") -> str:
            import urllib.parse

            return endpoint + urllib.parse.quote(ql_content)

        if kwargs.get("use_overpass_query"):
            # 先分source是api还是overpass
            # 再看target是区域还是单个/多个元素
            # 因为从API下载和从Overpass的逻辑天差地别，但元素还是区域的差异基本就是模板填空
            if kwargs.get("local_overpassql_path"):
                ql_file = open(
                    kwargs.get("local_overpassql_path"),
                    "r",
                    encoding="utf-8",
                )
                ql_content = ql_file.read()
                ql_file.close()
            else:
                ql_content = query("", "Overpass")
            work_url = url_of_overpass_quary(ql_content, "osmde")

        if target != "":
            if target == "area":
                # parse SWNE
                S = kwargs.get("S") if kwargs.get("S") else 0.0
                W = kwargs.get("W") if kwargs.get("W") else 0.0
                N = kwargs.get("N") if kwargs.get("N") else 0.0
                E = kwargs.get("E") if kwargs.get("E") else 0.0
                # call
                work_url = self.read_network_area(
                    source=source, endpoint=endpoint, S=S, W=W, N=N, E=E
                )
            else:
                if kwargs.get("element_id"):
                    # 但element_id是单个还是多个也不知道
                    work_url = self.read_network_element(
                        element_id=kwargs["element_id"],
                        element_type=kwargs.get("type"),
                        endpoint=endpoint,
                    )
                else:
                    # parse Element
                    pass
        else:
            if kwargs.get("url"):
                # download directly, then judge
                work_url = ""
            else:
                return None
        # run worker
        log.info(work_url)
        work_load_cache_path = os.path.join(
            get_yuheng_path(), "cache", get_cache_filename(work_url)
        )
        if kwargs.get("allow_cache", False) == True and os.path.exists(
            work_load_cache_path
        ):
            with open(
                work_load_cache_path,
                "r",
                encoding="utf-8",
            ) as f_work_load:
                work_load = f_work_load.read()
            self.read_memory(work_load)
        else:
            work_load = worker(
                work_url=work_url, allow_cache=kwargs.get("allow_cache", True)
            )
            self.read_memory(work_load)

    def read_network_area(
        self, S, W, N, E, source="api", endpoint="osm"
    ) -> str:
        """
        仅限API读取。
        另可参考 https://github.com/enzet/map-machine/blob/main/map_machine/osm/osm_getter.py
        """
        work_url = f"{get_endpoint_api(endpoint_name=endpoint)}/0.6/map?bbox={W},{S},{E},{N}"
        return work_url

    def read_network_element(
        self,
        element_id: Union[List[str], str],
        element_type="undefined",
        source="api",
        endpoint="osm",
    ) -> str:
        """
        仅限API读取。
        一个不管single/multi都能生成url的read_network_element。
        * element_id: it can be string or list, but we will normalize it to list.
        """

        work_url = ""

        def element_id_normalizer(element_id_object: Union[List[str], str]):
            element_id_list = []

            def have_multi_elements(element_id_string: str) -> bool:
                if "," in element_id:
                    # have comma or space between multi element
                    return True

            if isinstance(element_id_object, list):
                return element_id_object
            else:
                if have_multi_elements(element_id_object):
                    # should split it and append
                    return element_id_list
                else:
                    return [element_id_object]

        if (
            prefix_normalization(element_type) == "node"
            or prefix_normalization(element_type) == "way"
            or prefix_normalization(element_type) == "relation"
        ):
            element_id = element_id_normalizer(element_id)
            # log.debug(element_id_normalizer(element_id))
            if len(element_id) == 1:
                pure_id = (
                    element_id[0]
                    .replace("n", "")
                    .replace("w", "")
                    .replace("r", "")
                )
                if "v" in pure_id:
                    version = pure_id.split("v")[1]
                    pure_id = pure_id.split("v")[0]

                log.info(endpoint)
                work_url = (
                    get_endpoint_api(endpoint_name=endpoint)
                    + "/"
                    + str(
                        get_endpoint_api(
                            endpoint_name=endpoint, property="version"
                        )
                    )
                    + "/"
                    + prefix_normalization(element_type, mode="p2prefix")
                    + "/"
                    + pure_id
                )
            else:
                pure_id_list = [
                    id.replace("n", "").replace("w", "").replace("r", "")
                    for id in element_id
                ]
                # log.debug(pure_id_list)
                work_url = (
                    get_endpoint_api(endpoint_name=endpoint)
                    + "/"
                    + str(
                        get_endpoint_api(
                            endpoint_name=endpoint, property="version"
                        )
                    )
                    + "/"
                    + prefix_normalization(
                        element_type, mode="p2prefix", plural=True
                    )
                    + "?"
                    + prefix_normalization(
                        element_type, mode="p2prefix", plural=True
                    )
                    + "="
                    + ",".join(pure_id_list)
                )

        else:
            # detect element_type single request
            # warn that if parameter element_type and element_id implied element_type don't match
            pass

        return work_url

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
            Carto.__set_attrib(element.attrib, "minlat", i.min_lat)
            Carto.__set_attrib(element.attrib, "minlon", i.min_lon)
            Carto.__set_attrib(element.attrib, "maxlat", i.max_lat)
            Carto.__set_attrib(element.attrib, "maxlon", i.max_lon)
            Carto.__set_attrib(element.attrib, "origin", i.origin)
            root.append(element)

        def base_osm_model_to_xml(
            tag_name: str, model: BaseOsmModel
        ) -> Element:
            tag: Element = Element(tag_name)
            tag.attrib["id"] = str(model.id)
            Carto.__set_attrib(tag.attrib, "action", model.action)
            Carto.__set_attrib(tag.attrib, "timestamp", model.timestamp)
            Carto.__set_attrib(tag.attrib, "uid", model.uid)
            Carto.__set_attrib(tag.attrib, "user", model.user)
            tag.attrib["visible"] = "true" if model.visible else "false"
            Carto.__set_attrib(tag.attrib, "version", model.version)
            Carto.__set_attrib(tag.attrib, "changeset", model.changeset)
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
                log.info([member.type, member.ref, member.role, member.id])
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
        min_id = min_id if min_id < 0 else int(YUHENG_START_ID)
        return min_id - 1

    def flush(self, id: str) -> None:
        """
        传入形如"n123,w456,r789"的字符串，并批量执行flush
        """
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

    def clip(self) -> "Carto":
        """
        world=Carto().clip(condiation)
        condiation can be:

        country_or_region_code (use built-in geojson)
        user_defined.geojson
        user_defined.poly
        bbox
        (point,radius) tuple or dict/list/2_arguments

        maybe we need to create a boundary Class and OSM bound Class inherit from it.
        """
        pass
