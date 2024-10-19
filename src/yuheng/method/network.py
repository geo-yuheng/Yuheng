"""
network 模块并不负责从网上读取数据，它负责的是endpoint和各种网络相关环境的处理。而从网络上读取数据是作为read driver的一种（因为并不仅仅有一种来源的driver）
"""

from typing import Optional

from ..basic import YUHENG_CORE_NAME, YUHENG_VERSION
from ..basic.environment import get_ua


def get_endpoint_api(endpoint_name="osm", property="url") -> Optional[str]:
    endpoint_api_list = {
        "osm": {"url": "https://api.openstreetmap.org/api", "version": 0.6},
        "ogf": {"url": "https://opengeofiction.net/api", "version": 0.6},
        "ohm": {
            "url": "https://www.openhistoricalmap.org/api",
            "version": 0.6,
        },
        "osm-api06": {
            "url": "https://api06.dev.openstreetmap.org/api",
            "version": 0.6,
        },
        "osm-dev": {
            "url": "https://master.apis.dev.openstreetmap.org/api",
            "version": 0.6,
        },
    }
    return endpoint_api_list.get(endpoint_name.lower()).get(property)


def get_endpoint_overpass(
    endpoint_name="osmde", property="url"
) -> Optional[str]:
    endpoint_overpass_list = {
        "osmde": {
            "server": "osm",
            "url": "https://overpass-api.de/api/",
            "region": "global",
            "version": "unknown",
        },
        "kumi": {
            "server": "osm",
            "url": "https://overpass.kumi.systems/api/",
            "region": "global",
            "version": "unknown",
        },
        "osmru": {
            "server": "osm",
            "url": "http://overpass.openstreetmap.ru/cgi/",
            "region": "global",
            "version": "unknown",
        },
        "osmfr": {
            "server": "osm",
            "url": "https://overpass.openstreetmap.fr/api/",
            "region": "global",
            "version": "unknown",
        },
        "ogf": {
            "server": "ogf",
            "url": "https://overpass.ogf.rent-a-planet.com/api/",
            "region": "global",
            "version": "unknown",
        },
        "ohm": {
            "server": "ohm",
            "url": "https://overpass-api.openhistoricalmap.org/api/",
            "region": "global",
            "version": "unknown",
        },
    }

    return endpoint_overpass_list.get(endpoint_name.lower()).get(property)


def get_headers() -> dict:
    """
    Generate custom headers for HTTP requests.

    The custom headers include the User-Agent, which is a combination of
    YUHENG_CORE_NAME and YUHENG_VERSION (if possible and necessary, add the latest git commit hash).

    :return: A dictionary containing the custom headers.
    """
    return {
        "User-Agent": get_ua()  # if possible and necessary, add latest git commit hash
    }
