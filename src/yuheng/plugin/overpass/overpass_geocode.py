# note that there maybe another method to restrict workign area and use relation id directly.
# https://wiki.openstreetmap.org/w/index.php?title=Key:default_language&diff=next&oldid=2446989

def overpass_geocode_transform(id=None, keyword=None) -> int:
    return 3600 * 1000000 + 1


def overpass_geocode_replace():
    """
    Usage:
    Offer a one-click function to transform in a AreaSearch overpassql(allow both file IO and memory read)
    """

    # 1. search and parse AreaSearch part in QL
    # 2. import nominatim_request and get result list (def nominatim_request)
    # 3. use first result and calc real id (def geocode_transform)
    pass
