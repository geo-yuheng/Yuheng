from typing import Optional

from ..basic import KEQING_CORE_NAME, KEQING_VERSION


# from src.keqing.basic.global_const import KEQING_CORE_NAME, KEQING_VERSION


def get_server(server_name: str) -> Optional[str]:
    server_list = {
        "OSM": {"url": "https://api.openstreetmap.org/api/0.6/"},
        "OGF": {"url": "https://opengeofiction.net/api/0.6/"},
        "OHM": {"url": "https://www.openhistoricalmap.org/api/0.6"},
    }
    return server_list.get(server_name)["url"]


def get_overpass(overpass_name: str, server="") -> Optional[str]:
    overpass_list = {
        "osmde": {
            "server": "OSM",
            "url": "https://overpass-api.de/api/",
            "region": "global",
            "version": "unknown",
        },
        "kumi": {
            "server": "OSM",
            "url": "https://overpass.kumi.systems/api/",
            "region": "global",
            "version": "unknown",
        },
        "osmru": {
            "server": "OSM",
            "url": "http://overpass.openstreetmap.ru/cgi/",
            "region": "global",
            "version": "unknown",
        },
        "osmfr": {
            "server": "OSM",
            "url": "https//overpass.openstreetmap.fr/api/",
            "region": "global",
            "version": "unknown",
        },
        "ogf": {
            "server": "OGF",
            "url": "https//overpass.ogf.rent-a-planet.com/api/",
            "region": "global",
            "version": "unknown",
        },
        "ohm": {
            "server": "OHM",
            "url": "https://overpass-api.openhistoricalmap.org/api/",
            "region": "global",
            "version": "unknown",
        },
    }

    if server != "":
        if (
            overpass_list.get(overpass_name) != None
            and overpass_list.get(overpass_name)["server"] != server
        ):
            return overpass_list.get(overpass_name)["url"]
        else:
            return None
    else:
        return overpass_list.get(overpass_name)["url"]


def get_headers() -> dict:
    """
    Generate custom headers for HTTP requests.

    The custom headers include the User-Agent, which is a combination of
    KEQING_CORE_NAME and KEQING_VERSION (if possible and necessary, add the latest git commit hash).

    :return: A dictionary containing the custom headers.
    """
    return {
        "User-Agent": KEQING_CORE_NAME
        + "/ "
        + KEQING_VERSION  # if possible and necessary, add latest git commit hash
    }
