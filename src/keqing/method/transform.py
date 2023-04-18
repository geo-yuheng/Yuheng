# Waiting
def prefix_abbreviation(source: str, mode="p2prefix") -> str:
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
