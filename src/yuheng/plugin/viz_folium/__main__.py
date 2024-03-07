import os
import sys
import time
from typing import List, Tuple, Union, Optional

import folium

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import logger
from yuheng.component import Member, Node, Relation, Way


class VizFolium:
    def __init__(self):
        self.config_node_display_method = "marker"
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
        self,
        element: Union[Node, Way, Relation],
        element_type="",
        reference_carto=None,
    ) -> Union[Tuple[float, float], List[Tuple[float, float]]]:
        if element_type == "node" or isinstance(
            element, type(self.sample_node)
        ):
            lat = element.lat
            lon = element.lon
            return tuple([lat, lon])
        elif element_type == "way" or isinstance(
            element, type(self.sample_way)
        ):
            # optimization of processing line have room, but difficult
            nd_list = element.nds
            nd_shape_list = []
            node_space = self.element_list
            if reference_carto != None:
                node_space = [v for k, v in reference_carto.node_dict.items()]
            for node in nd_list:
                for iter_ele in node_space:
                    if (
                        isinstance(iter_ele, type(Node({"id": "114"}, {})))
                        and iter_ele.id == node
                    ):
                        nd_shape_list.append((iter_ele.lat, iter_ele.lon))
            return nd_shape_list

    def display(self, **kwargs) -> None:
        """
        This func display some element to html

        If **kwargs is not blank, then we should call self.add() for each one, then display as expected.

        Preserce argument:
        * default_center_lat:float
        * default_center_lon:float
        * default_zoom:int
        * colour_original: bool
        """
        logger.trace(__name__)
        import webbrowser

        preserve_argument = {
            "default_zoom": 0,
            "default_center_lat": 0.0,
            "default_center_lon": 0.0,
            "default_tiles": "",
            "default_attribution": "",
            "colour_original": False,
        }
        for k, v in preserve_argument.items():
            if (
                kwargs.get(k, None) != None
                and isinstance(kwargs.get(k), type(v)) != True
            ):
                logger.error(
                    f"You use preverse argument {k}, please check your usage!"
                )
                return None

        if (len(kwargs)) > 0:
            logger.info(f"There are {len(kwargs)} object need to append")
            for k, v in kwargs.items():
                self.add(v)

        m = folium.Map(
            location=[
                kwargs.get("default_center_lat", 0.0),
                kwargs.get("default_center_lon", 0.0),
            ],
            zoom_start=kwargs.get("default_zoom", 0),
        )
        # # You can replace with custom tiles
        # m = folium.Map(
        #     tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        #     attr=" ".join(
        #         [
        #             f'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        #             f'&copy; <a href="https://carto.com/attributions">CARTO</a>',
        #         ]
        #     ),
        # )

        for element in self.element_list:
            if isinstance(element, type(self.sample_node)):
                logger.debug("This is a Node")

                if self.config_node_display_method == "marker":
                    folium.Marker(list(self.transform(self, element))).add_to(
                        m
                    )
                elif self.config_node_display_method == "short_line":
                    folium.PolyLine(
                        [
                            self.transform(self, element),
                            self.transform(self, element),
                        ]
                    ).add_to(m)
                else:
                    pass

            if isinstance(element, type(self.sample_way)):
                logger.debug("This is a Way")
                folium.PolyLine(self.transform(self, element)).add_to(m)
            if isinstance(
                element,
                type(self.sample_relation),
            ):
                logger.debug("This is a Relation")
            if isinstance(element, type(self.sample_carto)):
                logger.debug("Wow a hole map!")
                # batch time control
                work_burden = (
                    len(element.node_dict)
                    + len(element.way_dict)
                    + len(element.relation_dict)
                )
                work_burden_report_node_interval = 1000
                work_burden_report_way_interval = 15
                work_burden_report_large_data = 1.5
                # node
                time_node_start = time.time()
                work_burden_node_count = 0
                for id, obj in element.node_dict.items():
                    # logger.debug(f"world-node-{id}")
                    work_burden_node_count += 1
                    folium.ColorLine(
                        positions=[(obj.lat, obj.lon), (obj.lat, obj.lon)],
                        colors=[0.114514, 0.1919810],
                        colormap=["black", "black"],
                        weight=4,
                    ).add_to(m)
                    if (
                        work_burden > work_burden_report_node_interval
                        and work_burden_node_count
                        % work_burden_report_node_interval
                        == 0
                    ):
                        time_node_this = time.time()
                        logger.info(
                            "[time] display "
                            + str(work_burden_node_count)
                            + " node use "
                            + str(round(time_node_this - time_node_start, 3))
                            + " s"
                        )
                time_node_end = time.time()
                logger.info(
                    "[time] display **all** node use "
                    + str(round(time_node_end - time_node_start, 3))
                    + " s"
                )
                # way
                if kwargs.get("colour_original", False) == True:
                    count_way_coloured = 0
                    count_way_uncoloured = 0
                time_way_start = time.time()
                work_burden_way_count = 0
                for id, obj in element.way_dict.items():
                    # logger.debug(f"world-way-{id} length={len(obj.nds)}")
                    # logger.debug(kwargs.get("colour_original", False))
                    # logger.debug(obj.tags.get("colour", None))
                    if len(obj.nds) >= 0:
                        work_burden_way_count += 1
                        time_this_way_start = time.time()
                        if kwargs.get("colour_original", False) == True:

                            def get_colour(
                                target_way_id: Union[int, str],
                                reference_carto: Carto,
                            ) -> Optional[str]:
                                if isinstance(target_way_id, str):
                                    target_way_id = int(target_way_id)

                                way_obj = reference_carto.way_dict[
                                    target_way_id
                                ]
                                if way_obj.tags.get("colour", None) != None:
                                    # colour on way itself
                                    return way_obj.tags["colour"]
                                else:
                                    # colour may defined on way's father relation
                                    # mainly on route relation in public transport career.
                                    for (
                                        relation_id,
                                        relation_obj,
                                    ) in reference_carto.relation_dict.items():
                                        for member in relation_obj.members:
                                            if (
                                                member.type == "way"
                                                and member.ref == target_way_id
                                            ):
                                                return relation_obj.tags.get(
                                                    "colour", None
                                                )

                            if get_colour(id, element) != None:
                                colour = get_colour(id, element)
                                logger.info(
                                    f"Colour {colour} was detected in w{id}"
                                )
                                position_list = self.transform(
                                    self, obj, reference_carto=element
                                )
                                folium.ColorLine(
                                    positions=position_list,
                                    colors=[
                                        float((i + 0.5) / len(position_list))
                                        for i in range(len(position_list))
                                    ],
                                    colormap=[colour, colour],
                                    weight=4,
                                ).add_to(m)
                                logger.debug(
                                    [
                                        float((i + 0.5) / len(position_list))
                                        for i in range(len(position_list))
                                    ]
                                )
                                count_way_coloured += 1
                            else:
                                position_list = self.transform(
                                    self, obj, reference_carto=element
                                )
                                folium.ColorLine(
                                    positions=position_list,
                                    colors=[
                                        float((i + 0.5) / len(position_list))
                                        for i in range(len(position_list))
                                    ],
                                    colormap=["black", "black"],
                                    weight=2,
                                ).add_to(m)
                                count_way_uncoloured += 1
                        else:
                            folium.PolyLine(
                                self.transform(
                                    self, obj, reference_carto=element
                                ),
                                weight=2,
                            ).add_to(m)
                        time_this_way_end = time.time()

                        if (
                            work_burden > work_burden_report_way_interval
                            and work_burden_way_count
                            % work_burden_report_way_interval
                            == 0
                        ):
                            time_way_this = time.time()
                            logger.info(
                                "[time] display "
                                + str(work_burden_way_count)
                                + " way use "
                                + str(round(time_way_this - time_way_start))
                                + " s"
                            )
                        # inspect large data (long way)
                        if (
                            time_this_way_end - time_this_way_start
                        ) >= work_burden_report_large_data:
                            logger.warning(
                                f"[time] w{obj.id} ({round(time_this_way_end - time_this_way_start,3)}s) "
                                f"have {len(obj.nds)} node and cause time "
                                f"longer than {work_burden_report_large_data} s"
                            )
                time_way_end = time.time()
                logger.info(
                    "[time] display **all** way use "
                    + str(round(time_way_end - time_way_start, 3))
                    + " s"
                )
                logger.debug(
                    f"work_burden_node_count={work_burden_node_count}"
                )
                logger.debug(f"work_burden_way_count={work_burden_way_count}")
                logger.debug(f"count_way_coloured={count_way_coloured}")
                logger.debug(f"count_way_uncoloured={count_way_uncoloured}")

        # gen html file or call webbrowser
        time_save_html_start = time.time()
        m.save("index.html")
        time_save_html_end = time.time()
        logger.info(
            "[time] save html use "
            + str(round(time_save_html_end - time_save_html_start, 3))
            + " s"
        )
        # webbrowser.open(
        #     url=os.path.join(
        #         os.path.dirname(os.path.realpath(__file__)), "index.html"
        #     ),
        #     new=1,
        # )
        return None

    def meow(self):
        logger.info(
            "\n"
            + "==========\n"
            + "This folium viz object have such elements\n"
            + "==========\n"
            + (str(len(self.element_list)) + "\n")
            + "==========\n"
        )


def main() -> None:
    logger.error("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
