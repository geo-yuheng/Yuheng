from typing import Dict, Optional


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
        return (
            self.type != self.__type_backup
            or self.ref != self.__ref_backup
            or self.role != self.__role_backup
        )
