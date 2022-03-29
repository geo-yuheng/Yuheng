from typing import Dict, Optional


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
        for key, new_value in self.tags.items():
            old_value = (
                self.__tags_backup[key] if key in self.__tags_backup else ""
            )
            if new_value != old_value:
                print(f"{key}=f{old_value} -> {key}={new_value}")
        for deleted_keys in self.__tags_backup.keys() - self.tags.keys():
            print(
                f"{deleted_keys}={self.__tags_backup[deleted_keys]} > {deleted_keys}= "
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
        self.__type_backup: str = type
        self.__ref_backup: int = ref
        self.__role_backup: str = role

    def has_diff(self) -> bool:
        return self.type != self.__type_backup or \
               self.ref != self.__ref_backup or \
               self.role != self.__role_backup
