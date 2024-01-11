from typing import Dict, Optional


class Bounds:
    def __init__(self, attrib: Dict[str, str]):
        self.min_lat: float = float(attrib["minlat"])
        self.min_lon: float = float(attrib["minlon"])
        self.max_lat: float = float(attrib["maxlat"])
        self.max_lon: float = float(attrib["maxlon"])
        self.origin: str = attrib.get("origin", "")

    def bound_serialization(
        self, serialize_format="SS_WW_NN_EE", escape=True
    ) -> str:
        """
        选择重复书写两次字母是因为避免单独的N出现。
        因为P/N被用于转义正负数，D被用于转义小数点

        常见顺序有多种，因此您应当指定输出顺序，否则使用默认顺序：
        * 在OSMAPI后端：https://www.openstreetmap.org/api/0.6/map?bbox=W,S,E,N
        * 在OverpassQL中：[bbox:south,west,north,east]
        """

        def num_serialization(degree: float, escape=True):
            if escape:
                if degree >= 0:
                    return "P" + str(degree).replace(".", "D")
                else:
                    return str(degree).replace("-", "N").replace(".", "D")
            else:
                return str(degree)

        return (
            serialize_format.replace("SS", num_serialization(self.min_lat))
            .replace("WW", num_serialization(self.min_lon))
            .replace("NN", num_serialization(self.max_lat))
            .replace("EE", num_serialization(self.max_lon))
        )

    def bound_deserialization(
        self, serialize_format="SS_WW_NN_EE"
    ):  # ->Tuple[float,float,float,float]:
        # return (min_lat,min_lon,max_lat,max_lon)
        pass


class Member:
    def __init__(self, element_type: str, role: str, ref=None, id=None):
        self.type: str = element_type
        self.role: str = role
        self.__type_backup: str = element_type
        self.__role_backup: str = role
        if (ref is not None) or (id is not None):
            if isinstance(ref, int):
                ref_value: int = ref
                id_value: int = ref
            elif isinstance(id, int):
                ref_value: int = id
                id_value: int = id
            else:
                print("Both 'ref' and 'id' isn't int.")
        else:
            print(
                "WARNING: Both 'ref' and 'id' haven't been offer while initializing Member class."
            )
        self.ref = ref_value
        self.id = id_value
        self.__ref_backup: int = ref_value
        self.__id_backup: int = id_value

    def has_diff(self) -> bool:
        return (
            self.type != self.__type_backup
            or self.ref != self.__ref_backup
            or self.role != self.__role_backup
        )
