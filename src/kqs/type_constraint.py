from typing import Dict, Optional


class Bounds:
    def __init__(self, attrib: Dict[str, str]):
        self.min_lat: float = float(attrib["minlat"])
        self.min_lon: float = float(attrib["minlon"])
        self.max_lat: float = float(attrib["maxlat"])
        self.max_lon: float = float(attrib["maxlon"])
        self.origin: str = attrib.get("origin", "")

    def align_serialization(self) -> str:
        serialize_format = "SB_WB_NB_EB"
        # another choise is don't use B in output_format, and use A/B insteal of P/N for plus or minus sign
        def num_serialization(degree: float):
            if degree >= 0:
                return "P" + str(degree).replace(".", "D")
            else:
                return str(degree).replace("-", "N").replace(".", "D")

        return (
            serialize_format.replace("SB", num_serialization(min_lat))
            .replace("WB", num_serialization(min_lon))
            .replace("NB", num_serialization(max_lat))
            .replace("EB", num_serialization(max_lon))
        )

    def align_serialization(self) -> str:
        serialize_format = "SB_WB_NB_EB"
        # another choise is don't use B in output_format, and use A/B insteal of P/N for plus or minus sign
        def num_serialization(degree: float):
            if degree >= 0:
                return "P" + str(degree).replace(".", "D")
            else:
                return str(degree).replace("-", "N").replace(".", "D")

        return (
            serialize_format.replace("SB", num_serialization(min_lat))
            .replace("WB", num_serialization(min_lon))
            .replace("NB", num_serialization(max_lat))
            .replace("EB", num_serialization(max_lon))
        )

    def align_deserialization(
        self, serialize_format="SB_WB_NB_EB"
    ):  # ->Tuple[float,float,float,float]:
        # return (min_lat,min_lon,max_lat,max_lon)
        pass


class Member:
    def __init__(self, type: str, ref: int, role: str):
        self.type: str = type
        self.ref: int = ref
        self.role: str = role
        self.id: int = ref # poka-yoke
        self.__type_backup: str = type
        self.__ref_backup: int = ref
        self.__role_backup: str = role
        self.__id_backup: int = ref # poka-yoke

    def has_diff(self) -> bool:
        return (
            self.type != self.__type_backup
            or self.ref != self.__ref_backup
            or self.role != self.__role_backup
        )
