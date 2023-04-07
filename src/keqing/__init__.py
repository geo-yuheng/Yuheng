import time
from typing import Dict, List

from keqing.basic.global_const import KEQING_CORE_NAME, KEQING_START_ID, KEQING_VERSION
from keqing.method.network import get_server, get_headers
from keqing.method.parse import parse_node, parse_way, parse_relation, pre_parse_classify
from keqing.method.stream_read import read_file, read_memory, read_network_area, read_network_element_batch, \
    read_network_element
from keqing.method.stream_write import write_file, write_network, write_josm_remote_control
from keqing.method.transform import prefix_abbreviation
from keqing.basic.model import BaseOsmModel
from keqing.type.constraint import Bounds, Member
from keqing.type.element import Node, Relation, Way


def meow(self):
    import logging
    logging.info(str(
        ("==============================\n")
        + ("Keqing load successful!\n")
        + ("==============================\n")
        + (
                str(len(self.node_dict))
                + str(len(self.way_dict))
                + str(len(self.relation_dict))
                + str(len(self.bounds_list))
        )
        + ("\n==============================")
    ))

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



    def read(self, mode=None, file_path="", text="", url="", fpath="", data_driver=""):
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
            read_file(self.node_dict, self.way_dict, self.relation_dict, self.bounds_list, file_path)
        elif (
            mode == "memory" or mode == "m" or mode == "text" or mode == "t"
        ) or ((mode == "file" or mode == "f") and file_path == ""):
            pre_read_warn(mode=mode, file_path=file_path, text=text, url=url)
            if file_path != "" and text != "":
                print(
                    "WARN:You add parameter for both file mode and memory mode! Keqing will choose you designated **memory** mode"
                )
            read_memory(self.node_dict, self.way_dict, self.relation_dict, self.bounds_list, text)
        elif mode == "network" or mode == "n":
            # pre_read_warn(mode=mode,file_path=file_path,text=text,url=url) # No need, we may need warn a 'mode="network" + url=""' situation.
            read_memory(self.node_dict, self.way_dict, self.relation_dict, self.bounds_list, url)
        else:
            raise TypeError(f"Unexpected read mode: {mode}")

        time_end = time.time()
        print("[TIME]: " + str(round((time_end - time_start), 3)) + "s" + "\n")
        meow()

    def write(mode=None, file_path="",
              data_driver=""):
        if mode == "file":
            write_file(version, generator, bounds_list, node_dict, way_dict,
                       relation_dict, file_path)
        elif mode == "network":
            write_network()
        elif mode == "josm_remote_control":
            # maybe remote_control_josm will be better?
            write_josm_remote_control()
        else:
            raise TypeError(f"Unexpected write mode: {mode}")

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
