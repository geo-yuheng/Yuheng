from typing import Dict, Optional, List
from xml.dom import minidom
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element

KQS_VERSION = "0.2.0"
KQS_GENERATOR = "Keqing_Sword"


class BaseOsmModel:
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        self.id: int = int(attrib.get('id'))
        self.action: Optional[str] = attrib.get('action')
        self.timestamp: Optional[str] = attrib.get('timestamp')
        self.uid: Optional[int] = int(attrib.get('uid')) if attrib.get('uid') is not None else None
        self.user: Optional[str] = attrib.get('user')
        self.visible: bool = bool(attrib.get('visible', 'True'))
        self.version: Optional[int] = int(attrib.get('version')) if attrib.get('version') is not None else None
        self.changeset: Optional[int] = int(attrib.get('changeset')) if attrib.get('changeset') is not None else None
        self.tags: Dict[str, str] = dict(tag_dict)
        self.tags_backup: Dict[str, str] = dict(tag_dict)

    def has_diff(self) -> bool:
        return self.tags != self.tags_backup

    def print_diff(self):
        print(self.tags['name'])
        print('变更：')
        for key, new_value in self.tags.items():
            old_value = self.tags_backup[key] if key in self.tags_backup else ''
            if new_value != old_value:
                print('%s=%s -> %s=%s' % (key, old_value, key, new_value))
        for deleted_keys in self.tags_backup.keys() - self.tags.keys():
            print('%s=%s > %s=%s' % (deleted_keys, self.tags_backup[deleted_keys], deleted_keys, ''))
        print('==========================================')


class Bounds:
    def __init__(self, attrib: Dict[str, str]):
        self.min_lat: float = float(attrib['minlat'])
        self.min_lon: float = float(attrib['minlon'])
        self.max_lat: float = float(attrib['maxlat'])
        self.max_lon: float = float(attrib['maxlon'])
        self.origin: str = attrib['origin']


class Member:
    def __init__(self, type: str, ref: int, role: str):
        self.type: str = type
        self.ref: int = ref
        self.role: str = role


class Node(BaseOsmModel):
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str]):
        super().__init__(attrib, tag_dict)
        self.lat: float = float(attrib['lat'])
        self.lon: float = float(attrib['lon'])


class Way(BaseOsmModel):
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str], nd_list: List[int]):
        super().__init__(attrib, tag_dict)
        self.nds: List[int] = nd_list.copy()


class Relation(BaseOsmModel):
    def __init__(self, attrib: Dict[str, str], tag_dict: Dict[str, str], member_list: List[Member]):
        super().__init__(attrib, tag_dict)
        self.members: List[Member] = member_list.copy()


class Waifu:
    def __init__(self):
        self.version: str = KQS_VERSION
        self.generator: str = KQS_GENERATOR
        self.bounds_list: List[Bounds] = []
        self.node_dict: Dict[int, Node] = {}
        self.way_dict: Dict[int, Way] = {}
        self.relation_dict: Dict[int, Relation] = {}

    @staticmethod
    def __set_attrib(attrib: Dict[str, str], key: str, value):
        if value is not None:
            attrib[key] = str(value)

    def __parse_node(self, element: Element):
        attrib: Dict[str, str] = element.attrib
        tag_dict: Dict[str, str] = {}
        for sub_element in element:
            tag_dict[sub_element.attrib['k']] = sub_element.attrib['v']
        self.node_dict[int(attrib['id'])] = Node(attrib, tag_dict)

    def __parse_way(self, element: Element):
        attrib: Dict[str, str] = element.attrib
        tag_dict: Dict[str, str] = {}
        nd_list: List[int] = []

        for sub_element in element:
            if sub_element.tag == 'nd':
                nd_list.append(int(sub_element.attrib['ref']))
            elif sub_element.tag == 'tag':
                tag_dict[sub_element.attrib['k']] = sub_element.attrib['v']
            else:
                raise TypeError('Unexpected element tag type: ' + sub_element.tag + ' in Way')
        self.way_dict[int(attrib['id'])] = Way(attrib, tag_dict, nd_list)

    def __parse_relation(self, element: Element):
        attrib: Dict[str, str] = element.attrib
        tag_dict: Dict[str, str] = {}
        member_list: List[Member] = []

        for sub_element in element:
            if sub_element.tag == 'member':
                member_list.append(
                    Member(
                        sub_element.attrib['type'],
                        int(sub_element.attrib['ref']),
                        sub_element.attrib['role']
                    )
                )
            elif sub_element.tag == 'tag':
                tag_dict[sub_element.attrib['k']] = sub_element.attrib['v']
            else:
                raise TypeError('Unexpected element tag type: ' + sub_element.tag + ' in Relation')
        self.relation_dict[int(attrib['id'])] = Relation(attrib, tag_dict, member_list)

    def from_file(self, file_path: str):
        tree: ElementTree = ET.parse(file_path)
        root: Element = tree.getroot()
        for element in root:
            if element.tag == 'node':
                self.__parse_node(element)
            elif element.tag == 'way':
                self.__parse_way(element)
            elif element.tag == 'relation':
                self.__parse_relation(element)
            elif element.tag == 'bounds':
                self.bounds_list.append(Bounds(element.attrib))
            else:
                #raise TypeError('Unexpected element tag type: ' + element.tag)
                pass

    def write(self, file_path: str):
        root: Element = Element("osm")
        root.attrib['version'] = self.version
        root.attrib['generator'] = self.generator

        for i in self.bounds_list:
            element: Element = Element("bounds")
            PyOsm.__set_attrib(element.attrib, 'minlat', i.min_lat)
            PyOsm.__set_attrib(element.attrib, 'minlon', i.min_lon)
            PyOsm.__set_attrib(element.attrib, 'maxlat', i.max_lat)
            PyOsm.__set_attrib(element.attrib, 'maxlon', i.max_lon)
            PyOsm.__set_attrib(element.attrib, 'origin', i.origin)
            root.append(element)

        def base_osm_model_to_xml(tag_name: str, model: BaseOsmModel) -> Element:
            tag: Element = Element(tag_name)
            tag.attrib['id'] = str(model.id)
            PyOsm.__set_attrib(tag.attrib, 'action', model.action)
            PyOsm.__set_attrib(tag.attrib, 'timestamp', model.timestamp)
            PyOsm.__set_attrib(tag.attrib, 'uid', model.uid)
            PyOsm.__set_attrib(tag.attrib, 'user', model.user)
            tag.attrib['visible'] = 'true' if model.visible else 'false'
            PyOsm.__set_attrib(tag.attrib, 'version', model.version)
            PyOsm.__set_attrib(tag.attrib, 'changeset', model.changeset)
            for k, v in model.tags.items():
                sub_element: Element = Element("tag")
                sub_element.attrib['k'] = k
                sub_element.attrib['v'] = v
                tag.append(sub_element)
            return tag

        for i in self.node_dict.values():
            node: Element = base_osm_model_to_xml('node', i)
            node.attrib['lat'] = str(i.lat)
            node.attrib['lon'] = str(i.lon)
            root.append(node)
        for i in self.way_dict.values():
            way: Element = base_osm_model_to_xml('way', i)
            for ref in i.nds:
                e: Element = Element("nd")
                e.attrib['ref'] = str(ref)
                way.append(e)
            root.append(way)
        for i in self.relation_dict.values():
            relation = base_osm_model_to_xml('relation', i)
            for member in i.members:
                e: Element = Element("member")
                e.attrib['type'] = member.type
                e.attrib['ref'] = str(member.ref)
                e.attrib['role'] = member.role
                relation.append(e)
            root.append(relation)

        raw_text = ET.tostring(root)
        dom = minidom.parseString(raw_text)
        with open(file_path, "w", encoding='utf-8') as file:
            dom.writexml(file, indent="\t", newl="\n", encoding="utf-8")
