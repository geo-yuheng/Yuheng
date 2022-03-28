from typing import Dict, List

from .model import BaseOsmModel, Member


class Node(BaseOsmModel):
    upstream_way: list = [0]
    upstream_relation: list = [0]

    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        super().__init__(attrib, tag_dict)
        self.lat: float = float(attrib["lat"])
        self.lon: float = float(attrib["lon"])
        self.__lat_backup: float = float(attrib["lat"])
        self.__lon_backup: float = float(attrib["lon"])

    def has_diff(self) -> bool:
        return self.id < 0 or self.has_tag_diff() or self.__has_position_diff()

    def __has_position_diff(self) -> bool:
        return self.lat != self.__lat_backup or self.lon != self.__lon_backup

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
        self.__nds_backup: List[int] = nd_list.copy()

    def has_diff(self) -> bool:
        return self.id < 0 or self.has_tag_diff() or self.__has_member_diff()

    def __has_member_diff(self) -> bool:
        return self.nds != self.__nds_backup

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
        self.__members_backup: List[Member] = member_list.copy()

    def has_diff(self) -> bool:
        return self.id < 0 or self.has_tag_diff() or self.__has_member_diff()

    def __has_member_diff(self) -> bool:
        if self.members != self.__members_backup:
            return True
        for member in self.members:
            if member.has_diff():
                return True
        return False

    def get_tag_all(self):
        pass

    def get_tag_query(self):
        pass

    def get_upstream_relation(self, order=-1):
        if order == -1:
            return self.upstream_relation
        else:
            return self.upstream_relation[order]
