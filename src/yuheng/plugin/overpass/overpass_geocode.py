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