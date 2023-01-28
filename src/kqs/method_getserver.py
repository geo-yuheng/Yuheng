def get_server(server_name: str) -> str:
    server_list = {
        "OSM": "https://www.openstreetmap.org/api/0.6/",
        "OGF": "https://opengeofiction.net/api/0.6/",
        "OHM": "https://www.openhistoricalmap.org/api/0.6",
    }
    return server_list[server_name]
