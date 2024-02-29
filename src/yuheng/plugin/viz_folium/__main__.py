import os
import sys
from typing import Union

import folium

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.type import Node, Relation, Way


class VizFolium:
    def __init__(self):
        self.element_list = []

    def add(self, element: Union[Carto, Way, Node, Relation]) -> None:
        """
        Append some element to list
        """
        self.element_list.append(element)
        return None

    def display(self, **kwargs) -> None:
        """
        This func display some element to html

        If **kwargs is not blank, then we should call self.add() for each one, then display as expected.
        """

        m = folium.Map(location=[11.4, 51.4], zoom_start=0)

        for element in self.element_list:
            if isinstance(element, type(Way({"id": "114"}, {}, []))):
                print("This is a Way")
                folium.PolyLine([(11.4, 51.4), (11.4, 51.4)]).add_to(m)
                folium.Marker([11.4, 51.4]).add_to(m)

        # gen html file or call webbrowser
        m.save("index.html")
        return None


def main() -> None:
    print("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
