from typing import Dict, Optional, List

from kqs_waifu import Waifu

KQS_VERSION: str = "0.2.0"
KQS_GENERATOR: str = "Keqing_Sword"
KQS_START_ID: int = -20210217  # 👴和刻晴小姐的结婚纪念日🥰


class BaseOsmModel:
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        self.id: int = int(attrib.get("id"))
        self.action: Optional[str] = attrib.get("action")
        self.timestamp: Optional[str] = attrib.get("timestamp")
        self.uid: Optional[int] = (
            int(attrib.get("uid")) if attrib.get("uid") is not None else None
        )
        self.user: Optional[str] = attrib.get("user")
        self.visible: bool = bool(attrib.get("visible", "True"))
        self.version: Optional[int] = (
            int(attrib.get("version"))
            if attrib.get("version") is not None
            else None
        )
        self.changeset: Optional[int] = (
            int(attrib.get("changeset"))
            if attrib.get("changeset") is not None
            else None
        )
        self.tags: Dict[str, str] = dict(tag_dict)
        self.tags_backup: Dict[str, str] = dict(tag_dict)

    def has_diff(self) -> bool:
        return self.tags != self.tags_backup

    def print_diff(self):
        print(self.tags["name"])
        print("变更：")
        for key, new_value in self.tags.items():
            old_value = (
                self.tags_backup[key] if key in self.tags_backup else ""
            )
            if new_value != old_value:
                print(f"{key}=f{old_value} -> {key}={new_value}")
        for deleted_keys in self.tags_backup.keys() - self.tags.keys():
            print(
                f"{deleted_keys}={self.tags_backup[deleted_keys]} > {deleted_keys}= "
            )
        print("==========================================")


class Bounds:
    def __init__(self, attrib: Dict[str, str]):
        self.min_lat: float = float(attrib["minlat"])
        self.min_lon: float = float(attrib["minlon"])
        self.max_lat: float = float(attrib["maxlat"])
        self.max_lon: float = float(attrib["maxlon"])
        self.origin: str = attrib.get("origin", "")


class Member:
    def __init__(self, type: str, ref: int, role: str):
        self.type: str = type
        self.ref: int = ref
        self.role: str = role


class Node(BaseOsmModel):
    upstream_way: list = [0]
    upstream_relation: list = [0]

    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        super().__init__(attrib, tag_dict)
        self.lat: float = float(attrib["lat"])
        self.lon: float = float(attrib["lon"])

    def get_tag_all(self):
        pass

    def get_tag_query(self):
        pass

    def get_upstream_way(self, order=-1):
        if order == -1:
            return self.upstream_way
        else:
            return self.upstream_way[order]

    def get_upstream_relation(self, order=-1):
        if order == -1:
            return self.upstream_relation
        else:
            return self.upstream_relation[order]


class Way(BaseOsmModel):
    upstream_relation: list = [0]

    def __init__(
        self,
        attrib: Dict[str, str],
        tag_dict: Dict[str, str],
        nd_list: List[int],
    ):
        super().__init__(attrib, tag_dict)
        self.nds: List[int] = nd_list.copy()

    def get_tag_all(self):
        pass

    def get_tag_query(self):
        pass

    def get_upstream_relation(self, order=-1):
        if order == -1:
            return self.upstream_relation
        else:
            return self.upstream_relation[order]


class Relation(BaseOsmModel):
    upstream_relation: list = [0]

    def __init__(
        self,
        attrib: Dict[str, str],
        tag_dict: Dict[str, str],
        member_list: List[Member],
    ):
        super().__init__(attrib, tag_dict)
        self.members: List[Member] = member_list.copy()

    def get_tag_all(self):
        pass

    def get_tag_query(self):
        pass

    def get_upstream_relation(self, order=-1):
        if order == -1:
            return self.upstream_relation
        else:
            return self.upstream_relation[order]
