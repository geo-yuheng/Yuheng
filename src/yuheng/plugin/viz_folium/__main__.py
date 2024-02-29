import os
import sys
from typing import Union, Tuple, List

import folium

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.type import Node, Relation, Way, Member


class VizFolium:
    def __init__(self):
        self.element_list = []
        self.sample_node = Node({"id": "114"}, {})
        self.sample_way = Way({"id": "514"}, {}, [])
        self.sample_relation = Relation(
            {"id": "1919"},
            {},
            [
                Member(
                    element_type="node",
                    role="vip_restaurant",
                    ref=810,
                )
            ],
        )
        self.sample_carto = Carto()

    def add(self, element: Union[Carto, Way, Node, Relation]) -> None:
        """
        Append some element to list
        """
        self.element_list.append(element)
        return None

    @staticmethod
    def transform(
        element: Union[Node, Way, Relation], element_type=""
    ) -> Union[Tuple[float, float], List[Tuple[float, float]]]:
        if element_type == "node" or isinstance(element, self.sample_node):
            lat = element.lat
            lon = element.lon
            return (lat, lon)

    def display(self, **kwargs) -> None:
        """
        This func display some element to html

        If **kwargs is not blank, then we should call self.add() for each one, then display as expected.
        """
        import webbrowser

        if (len(kwargs)) > 0:
            print(f"There are {len(kwargs)} object need to append")
            for k, v in kwargs.items():
                self.add(v)

        m = folium.Map(location=[0, 0], zoom_start=0)

        for element in self.element_list:
            if isinstance(element, type(self.sample_node)):
                print("This is a Node")
                node_display_method = "marker"

                if node_display_method == "marker":
                    folium.Marker(list(transform(element))).add_to(m)
                elif node_display_method == "short_line":
                    folium.PolyLine(
                        [transform(element), transform(element)]
                    ).add_to(m)
                else:
                    pass

            if isinstance(element, type(self.sample_way)):
                print("This is a Way")
                nd_list = element.nds
                nd_shape_list = []
                for node in nd_list:
                    for iter_ele in self.element_list:
                        if (
                            isinstance(iter_ele, type(Node({"id": "114"}, {})))
                            and iter_ele.id == node
                        ):
                            nd_shape_list.append((iter_ele.lat, iter_ele.lon))

                folium.PolyLine(nd_shape_list).add_to(m)
            if isinstance(
                element,
                type(self.sample_relation),
            ):
                print("This is a Relation")
            if isinstance(element, type(self.sample_carto)):
                print("Wow a hole map!")

        # gen html file or call webbrowser
        m.save("index.html")
        # webbrowser.open(
        #     url=os.path.join(
        #         os.path.dirname(os.path.realpath(__file__)), "index.html"
        #     ),
        #     new=1,
        # )
        return None


def main() -> None:
    print("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
