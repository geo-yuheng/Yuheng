from typing import Dict, Optional


class BaseOsmModel:
    # 仅用作历史兼容，merge后移除
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

    # 其他方法应尽快完善

    def flush(self):
        # 移除自身，但如果有被编辑应给予警告，在force的情况下可以强制从数据库中移除，即调用析构函数
        pass
