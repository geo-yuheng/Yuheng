from typing import Optional


def prefix_normalization(source: str, mode="p2prefix") -> str:
    if mode == "p2prefix":
        if source == "n" or source == "node":
            return "node"
        if source == "w" or source == "way":
            return "way"
        if source == "r" or source == "relation":
            return "relation"
        if source == "c" or source == "changeset":
            return "changeset"
        if source == "v" or source == "version":
            return "version"
    elif mode == "prefix2p":
        if source == "n" or source == "node":
            return "n"
        if source == "w" or source == "way":
            return "w"
        if source == "r" or source == "relation":
            return "r"
        if source == "c" or source == "changeset":
            return "c"
        if source == "v" or source == "version":
            return "v"


def prefix_judgement(object_id: str) -> Optional[str]:
    if (
        object_id[0] == "n"
        or object_id[0] == "w"
        or object_id[0] == "r"
        or object_id[0] == "c"
        or object_id[0] == "v"
    ):
        return prefix_normalization(object_id[0])
    else:
        return None
