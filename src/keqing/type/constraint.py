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

    def align_deserialization(
        self, serialize_format="SB_WB_NB_EB"
    ):  # ->Tuple[float,float,float,float]:
        # return (min_lat,min_lon,max_lat,max_lon)
        pass


class Member:
    def __init__(self, element_type: str, role: str, ref=None, id=None):
        self.type: str = element_type
        self.role: str = role
        self.__type_backup: str = element_type
        self.__role_backup: str = role
        if ref is None:
            if id is None:
                print(
                    "WARNING: Both 'ref' and 'id' haven't been offer while initializing Member class."
                )
        else:
            if isinstance(ref, int):
                print("ref is not None")
                ref_value: int = ref
                id_value: int = ref
            elif isinstance(id, int):
                print("id is not None")
                ref_value: int = id
                id_value: int = id
            else:
                print("Both 'ref' and 'id' isn't int.")

        print(self.__dir__())
        print(ref_value, id_value)
        self.__ref_backup: int = ref
        self.__id_backup: int = id

    def has_diff(self) -> bool:
        return (
            self.type != self.__type_backup
            or self.ref != self.__ref_backup
            or self.role != self.__role_backup
        )
