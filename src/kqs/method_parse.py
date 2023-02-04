# Waiting
def t2type(t: str) -> str:
    if t == "n" or t == "node":
        return "node"
    if t == "w" or t == "way":
        return "way"
    if t == "r" or t == "relation":
        return "relation"
    if t == "c" or t == "changeset":
        return "changeset"
    if t == "v" or t == "version":
        return "version"
