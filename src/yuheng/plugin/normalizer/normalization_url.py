def url_parse(url: str, domain: str = "openstreetmap.org"):
    type: str = "node"
    id: int = 0
    #     import urlib
    url = url.split(domain)
    # test case
    # openstreetmap.org/node/5739239358
    # http://www.openstreetmap.org/node/5739239358
    # https://www.openstreetmap.org/node/5739239358#map=19/25.53658/113.53478
    # https://www.openstreetmap.org/node/5739239358#map=19/25.53658/113.53444&layers=TNDG
    # https://www.openstreetmap.org/node/5739239358?locale=zh-TW#map=19/25.53658/113.53444
    # https://www.openstreetmap.org/node/5739239358/history#map=19/25.53668/113.53436
    # https://www.openstreetmap.org/way/639195258?mlat=31.594384&mlon=34.7861726#map=12/31.5964/34.8009
    # https://www.openstreetmap.org/query?lat=31.59385&lon=34.78639#map=18/31.59449/34.78754
    # https://www.openstreetmap.org/node/114/history/1
    # https://www.openstreetmap.org/search?whereami=1&query=59.95170%252C10.78680
    # https://www.openstreetmap.org/directions?engine=graphhopper_car&route=35.6026%2C140.1196%3B35.4445%2C139.6361#map=11/35.5685/139.8717
    return [type, id]


parse_url_fallback = [
    "osm.org",
    "openstreetmap.org",
    "openstreetmap.com",
]  # parse this js file https://github.com/openstreetmap/dns/blob/master/dnsconfig.js
