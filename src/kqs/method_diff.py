from kqs.type_constraint import Bounds, Member
from kqs.type_data import OSC, OSH, OSM
from kqs.type_element import Node, Relation, Way


class Diff:
    diff_pair_dict = []

    def __init__(self, data=None, element=None, constraint=None) -> None:
        if type(data) == type(OSM()):
            # Diff OSM
            self.print_diff(data)
        elif type(data) == type(OSC()):
            # Diff OSC
            pass
        elif type(data) == type(OSH()):
            # Diff OSH
            pass
        elif type(element) == type(Node()):
            # Diff Node
            pass
        elif type(element) == type(Way()):
            # Diff Way
            pass
        elif type(element) == type(Relation()):
            # Diff Relation
            pass
        elif type(constraint) == type(Bounds()):
            # Diff Bounds
            pass
        elif type(constraint) == type(Member()):
            # Diff Member
            pass
        else:
            raise Exception("Unknown type")

    def print():
        pass

    def print_diff(data):
        # old BaseOsmModel's function
        print(data.tags["name"])
        print("变更：")
        for key, value_new in data.tags.items():
            value_old = (
                data.__tags_backup[key] if key in data.__tags_backup else ""
            )
            if value_new != value_old:
                print(f"{key}=f{value_old} -> {key}={value_new}")
        for keys_deleted in data.__tags_backup.keys() - data.tags.keys():
            print(
                f"{keys_deleted}={data.__tags_backup[keys_deleted]} > {keys_deleted}= "
            )
        print("==========================================")
