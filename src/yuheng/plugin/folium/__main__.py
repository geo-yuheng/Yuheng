import os
import sys
from typing import Union

import folium

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu, Way, Node, Relation


def display(element: Union[Waifu, Way, Node, Relation]) -> None:
    if isinstance(element, type(Way())):
        pass
    return None


def main() -> 1:
    print("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
