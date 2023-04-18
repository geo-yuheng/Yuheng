def url_parse(url: str, domain: str = "openstreetmap.org"):
    type: str = "node"
    id: int = 0
    #     import urlib
    url = url.split(domain)
    # test case
    # node/way/relation/changeset
    # openstreetmap.org/node/5739239358
    # 　http://www.openstreetmap.org/node/5739239358
    # https://www.openstreetmap.org/node/5739239358#map=19/25.53658/113.53478
    # 　https://www.openstreetmap.org/node/5739239358#map=19/25.53658/113.53444&layers=TNDG
    # 　https://www.openstreetmap.org/node/5739239358?locale=zh-TW#map=19/25.53658/113.53444
    # https://www.openstreetmap.org/node/5739239358/history#map=19/25.53668/113.53436
    return [type, id]


parse_url_fallback = [
    "osm.org",
    "openstreetmap.org",
    "openstreetmap.com",
]  # parse this js file https://github.com/openstreetmap/dns/blob/master/dnsconfig.js
