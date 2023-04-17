# Waiting
from xml.etree import ElementTree
from xml.etree.ElementTree import ElementTree, Element

import requests

from keqing.method.network import get_server, get_headers
from keqing.method.parse import pre_parse_classify
from keqing.method.transform import prefix_abbreviation


def read_file(node_dict, way_dict, relation_dict, bounds_list, file_path: str):
    tree: ElementTree = ET.parse(file_path)
    root: Element = tree.getroot()
    pre_parse_classify(node_dict, way_dict, relation_dict, bounds_list, root)


def read_memory(node_dict, way_dict, relation_dict, bounds_list, text: str):
    root: Element = ET.fromstring(text)
    pre_parse_classify(node_dict, way_dict, relation_dict, bounds_list, root)


def read_network_area(S, W, N, E, mode="api", server="OSM"):
    if mode == "api":
        # https://github.com/enzet/map-machine/blob/main/map_machine/osm/osm_getter.py
        # need to add server change function
        pass
    if mode == "overpass":
        pass
    pass


def read_network_element_batch(
        element_id=None, mode="api", server="OSM"
):
    # it can be string or list
    # https://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:_GET_/api/0.6/[nodes|ways|relations]?#parameters
    pass


def read_network_element(node_dict, way_dict, relation_dict, bounds_list,
                         element_id: str, type="undefined", mode="api", server="OSM"
                         ):
    def have_multi_elements(element_id) -> bool:
        if "," in element_id:
            # have comma or space between multi element
            return True

    if have_multi_elements(element_id):
        read_network_element_batch(element_id)
    else:
        if (
            (type == "node" or type == "n")
            or (type == "way" or type == "w")
            or (type == "relation" or type == "r")
        ):
            import requests

            pure_id = (
                element_id.replace("n", "")
                .replace("w", "")
                .replace("r", "")
            )
            if "v" in pure_id:
                version = pure_id.split("v")[1]
                pure_id = pure_id.split("v")[0]
            url = get_server(server) + prefix_abbreviation(type,mode="p2prefix") + "/" + pure_id
            headers = get_headers()
            print("url:", url)
            print("headers:", headers)
            response = requests.get(url=url, headers=headers).text
            print(response)
            read_memory(node_dict, way_dict, relation_dict, bounds_list, response)
        else:
            # detect type single request
            # warn that if parameter type and element_id implied type don't match
            pass


def read_network(node_dict, way_dict, relation_dict, bounds_list, mode="api", server="OSM", quantity="", enable_cache=False **kwargs):
    # version problem haven't been introduced
    if quantity != "":
        if quantity == "area":
            # parse SWNE
            read_network_area()
        else:
            if kwargs.get("element_id"):
                read_network_element(node_dict, way_dict, relation_dict, bounds_list,
                                     element_id=kwargs["element_id"],
                                     type=kwargs.get("type"),
                                     server=server,
                                     )
            else:
                # parse Element
                pass
    else:
        if kwargs.get("url"):
            # download directly, then judge
            pass
        else:
            return None
    pass