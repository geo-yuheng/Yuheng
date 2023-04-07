from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from keqing import Waifu
from keqing.basic.model import BaseOsmModel


def write_file(version, generator, bounds_list, node_dict, way_dict, relation_dict, file_path: str, only_diff=False):
    root: Element = Element("osm")
    root.attrib["version"] = version
    root.attrib["generator"] = generator

    for i in bounds_list:
        element: Element = Element("bounds")
        Waifu.__set_attrib(element.attrib, "minlat", i.min_lat)
        Waifu.__set_attrib(element.attrib, "minlon", i.min_lon)
        Waifu.__set_attrib(element.attrib, "maxlat", i.max_lat)
        Waifu.__set_attrib(element.attrib, "maxlon", i.max_lon)
        Waifu.__set_attrib(element.attrib, "origin", i.origin)
        root.append(element)

    def base_osm_model_to_xml(
        tag_name: str, model: BaseOsmModel
    ) -> Element:
        tag: Element = Element(tag_name)
        tag.attrib["id"] = str(model.id)
        Waifu.__set_attrib(tag.attrib, "action", model.action)
        Waifu.__set_attrib(tag.attrib, "timestamp", model.timestamp)
        Waifu.__set_attrib(tag.attrib, "uid", model.uid)
        Waifu.__set_attrib(tag.attrib, "user", model.user)
        tag.attrib["visible"] = "true" if model.visible else "false"
        Waifu.__set_attrib(tag.attrib, "version", model.version)
        Waifu.__set_attrib(tag.attrib, "changeset", model.changeset)
        for k, v in model.tags.items():
            sub_element: Element = Element("tag")
            sub_element.attrib["k"] = k
            sub_element.attrib["v"] = v
            tag.append(sub_element)
        return tag

    for i in node_dict.values():
        if i.has_diff() and i.action != "delete":
            i.action = "modify"
        node: Element = base_osm_model_to_xml("node", i)
        node.attrib["lat"] = str(i.lat)
        node.attrib["lon"] = str(i.lon)
        root.append(node)
    for i in way_dict.values():
        if i.has_diff() and i.action != "delete":
            i.action = "modify"
        way: Element = base_osm_model_to_xml("way", i)
        for ref in i.nds:
            e: Element = Element("nd")
            e.attrib["ref"] = str(ref)
            way.append(e)
        root.append(way)
    for i in relation_dict.values():
        if i.has_diff() and i.action != "delete":
            i.action = "modify"
        relation = base_osm_model_to_xml("relation", i)
        for member in i.members:
            e: Element = Element("member")
            e.attrib["type"] = member.type
            e.attrib["ref"] = str(member.ref)
            e.attrib["role"] = member.role
            relation.append(e)
        root.append(relation)

    raw_text = ET.tostring(root)
    dom = minidom.parseString(raw_text)
    with open(file_path, "w", encoding="utf-8") as file:
        dom.writexml(file, indent="\t", newl="\n", encoding="utf-8")


def write_network():
    # will imply in the future
    pass


def write_josm_remote_control():
    # Thanks to @AustinZhu's idea about this branch of output stream
    # will imply in the long future
    pass


