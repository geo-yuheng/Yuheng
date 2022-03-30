from typing import Dict, Optional

from kqs.constraint import Bounds, Member
from kqs.type import Node, Relation, Way


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
        # feat: If version miss, maybe it was redacted. For example: n1
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
        self.__tags_backup: Dict[str, str] = dict(tag_dict)

    def has_diff(self) -> bool:
        return self.id < 0 or self.has_tag_diff()

    def has_tag_diff(self) -> bool:
        return self.tags != self.__tags_backup

    def print_diff(self):
        print(self.tags["name"])
        print("变更：")
        for key, value_new in self.tags.items():
            value_old = (
                self.__tags_backup[key] if key in self.__tags_backup else ""
            )
            if value_new != value_old:
                print(f"{key}=f{value_old} -> {key}={value_new}")
        for keys_deleted in self.__tags_backup.keys() - self.tags.keys():
            print(
                f"{keys_deleted}={self.__tags_backup[keys_deleted]} > {keys_deleted}= "
            )
        print("==========================================")


class Base:
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        self.id: int = int(attrib.get("id"))
        self.action: Optional[str] = attrib.get("action")
        self.timestamp: Optional[str] = attrib.get("timestamp")
        self.uid: Optional[int] = (
            int(attrib.get("uid")) if attrib.get("uid") is not None else None
        )
        self.user: Optional[str] = attrib.get("user")
        self.visible: bool = bool(attrib.get("visible", "True"))
        # feat: If version miss, maybe it was redacted. For example: n1
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
        self.__tags_backup: Dict[str, str] = dict(tag_dict)


class OSM(Base):
    def __init__(self) -> None:
        super().__init__()


class OSH(Base):
    def __init__(self) -> None:
        super().__init__()


class OSC(Base):
    def __init__(self) -> None:
        super().__init__()

    def Modify():
        pass

    def Create():
        # Call create function to create them in memory
        pass

    def Delete():
        # If element already in memory, delete it. (And save other unfound id)
        pass


class Diff:
    diff_pair_dict = []

    def __init__(self, data=None, element=None, constraint=None) -> None:
        if type(data) == type(OSM()):
            # Diff OSM
            print_diff(data)
        elif type(data) == type(OSC()):
            # Diff OSC
            pass
        elif type(data) == type(OSH()):
            # Diff OSH
            pass
        elif type(element) == type(Node()):
            # Diff Node
            pass
        elif type(element) == type(Way()):
            # Diff Way
            pass
        elif type(element) == type(Relation()):
            # Diff Relation
            pass
        elif type(constraint) == type(Bounds()):
            # Diff Bounds
            pass
        elif type(constraint) == type(Member()):
            # Diff Member
            pass
        else:
            raise Exception("Unknown type")
            
    def print():
        pass

    def print_diff(data):
        # old BaseOsmModel's function
        print(data.tags["name"])
        print("变更：")
        for key, value_new in data.tags.items():
            value_old = (
                data.__tags_backup[key] if key in data.__tags_backup else ""
            )
            if value_new != value_old:
                print(f"{key}=f{value_old} -> {key}={value_new}")
        for keys_deleted in data.__tags_backup.keys() - data.tags.keys():
            print(
                f"{keys_deleted}={data.__tags_backup[keys_deleted]} > {keys_deleted}= "
            )
        print("==========================================")
