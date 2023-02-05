from typing import Dict, List

from .model_basic import Base, BaseOsmModel
from .type_constraint import Member


class Node(BaseOsmModel):
    upstream_way: list = [0]
    upstream_relation: list = [0]

    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        super().__init__(attrib, tag_dict)
        if not attrib.get("lat") and not attrib.get("lon"):
            attrib["action"] = "delete"
        else:
            self.lat: float = float(attrib["lat"])
            self.lon: float = float(attrib["lon"])
            self.__lat_backup: float = float(attrib["lat"])
            self.__lon_backup: float = float(attrib["lon"])

    def __str__(self):
        # 为避免<kqs.type_element.Node object at 0x0000021717B5AF70>这种不利于debug的内容，允许重载运算符，提供输出到文本的函数
        # 此外，为与在tag_dict中的手打做区分，可以考虑用类似prettytable之类的封装成表，带上id做表头，优化显示
        pass

    def has_diff(self) -> bool:
        # 未来不在Node/Way/Relation保留diff方法，由diff类完成
        return self.id < 0 or self.has_tag_diff() or self.__has_position_diff()

    def __has_position_diff(self) -> bool:
        # 未来不在Node/Way/Relation保留diff方法，由diff类完成
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

    def is_latest(self, version=None):
        # 在引入OSH以后，一个点多个版本将同时并存，访问时需要判断版本，select查询影响不打，但iterator迭代的时候可能需要考虑避免迭代到旧版本。
        # 可能需要引入一个array，在每个版本都提供一个指向其他任一版本的“指针”？（其实是遍历一遍找对应id+version双匹配吧）
        # 最新版本被redact的情况下尚不知如何正确处理版本号
        if version == None:
            version = self.version
        pass

    def find_latest(self):
        # return Node(background found latest version)
        pass

    def find_history(self):
        # 查找提供本id的元素的上下历史全集，需要后台查找，然后排序一个array返回
        # return list(Node())
        pass


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

    def __str__(self):
        # 为避免<kqs.type_element.Node object at 0x0000021717B5AF70>这种不利于debug的内容，允许重载运算符，提供输出到文本的函数
        # 此外，为与在tag_dict中的手打做区分，可以考虑用类似prettytable之类的封装成表，带上id做表头，优化显示
        pass

    def has_diff(self) -> bool:
        # 未来不在Node/Way/Relation保留diff方法，由diff类完成
        return self.id < 0 or self.has_tag_diff() or self.__has_member_diff()

    def __has_member_diff(self) -> bool:
        # 未来不在Node/Way/Relation保留diff方法，由diff类完成
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

    def __str__(self):
        # 为避免<kqs.type_element.Node object at 0x0000021717B5AF70>这种不利于debug的内容，允许重载运算符，提供输出到文本的函数
        # 此外，为与在tag_dict中的手打做区分，可以考虑用类似prettytable之类的封装成表，带上id做表头，优化显示
        pass

    def has_diff(self) -> bool:
        # 未来不在Node/Way/Relation保留diff方法，由diff类完成
        return self.id < 0 or self.has_tag_diff() or self.__has_member_diff()

    def __has_member_diff(self) -> bool:
        # 未来不在Node/Way/Relation保留diff方法，由diff类完成
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
