from typing import Optional


def prefix_normalization(source: str, mode="p2prefix", plural=False) -> str:
    if mode == "p2prefix":
        if source == "n" or source == "node":
            if plural == False:
                return "node"
            else:
                return "nodes"
        if source == "w" or source == "way":
            if plural == False:
                return "way"
            else:
                return "ways"
        if source == "r" or source == "relation":
            if plural == False:
                return "relation"
            else:
                return "relations"
        if source == "c" or source == "changeset":
            if plural == False:
                return "changeset"
            else:
                return "changesets"
        if source == "v" or source == "version":
            if plural == False:
                return "version"
            else:
                return "versions"
    elif mode == "prefix2p":
        if source in ["n", "node", "nodes"]:
            return "n"
        if source in ["w", "way", "nodes"]:
            return "w"
        if source in ["r", "relation", "relations"]:
            return "r"
        if source in ["c", "changeset", "changesets"]:
            return "c"
        if source in ["v", "version", "versions"]:
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
