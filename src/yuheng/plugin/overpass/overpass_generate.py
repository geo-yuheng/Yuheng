from typing import Optional, Union

query_template = "<metadata_part>\n<condition_part>\n<output_part>"


def gen_metadata(**kwargs) -> Optional[str]:
    buffer = ""

    def wrap_metadata(key: str, value: Union[str, int, float]) -> str:
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return f"[{key}:{value}]"

    query_option_key = [
        "amenity",
        "name",
        "name:en",
        "short_name",
        "addr:province",
        "operators",
    ]
    OVERPASS_QL_CONTENTcsv = """
[out:csv(
    ::type,
    ::id,{{键}};
    true; "|"
)];"""

    OVERPASS_QL_CONTENTcsv.replace(
        "{{键}}", ",".join(['"' + i + '"' for i in query_option_key])
    )

    if kwargs.get("metadata_entry_data"):
        for metadata_entry_key in kwargs.get("metadata_entry_data"):
            metadata_entry_value = kwargs.get("metadata_entry_data").get(
                metadata_entry_key, ""
            )
            # possible value for out:
            # * xml
            # * json
            # * csv
            # * custom
            # * popup
            if metadata_entry_key == "out" and metadata_entry_value in [
                "xml",
                "json",
            ]:
                buffer += wrap_metadata(
                    metadata_entry_key, metadata_entry_value
                )
                # There should be a lint about final part after output format detected, I guess, such as geom/meta/body.
            elif metadata_entry_key == "out" and metadata_entry_value == "csv":
                pass
            elif metadata_entry_key == "out" and metadata_entry_value in [
                "custom",
                "popup",
            ]:
                print(
                    "This kind of output format will lead to a OSM3S Response, which currently not supported by Yuheng."
                    + "See more about this format in https://github.com/drolbr/Overpass-API/"
                )
            else:
                buffer += wrap_metadata(
                    metadata_entry_key, metadata_entry_value
                )
    if buffer != "":
        return buffer + ";"
    else:
        return None


def gen_constraint(constraint_type: str) -> str:
    if constraint_type == "none":
        constraint_content = ""
    elif constraint_type == "bbox":
        constraint_content = gen_bbox()
    elif constraint_type == "geoarea":
        constraint_content = gen_geocode()
    elif constraint_type == "poly":
        constraint_content = gen_poly()
    else:
        constraint_content = ""
    return constraint_content


def gen_query():
    return (
        query_template.replace("<metadata_part>", gen_metadata())
        .replace("<condition_part>", gen_condition())
        .replace("<output_part>", gen_output())
    )


testcase_gen_metadata = gen_metadata(
    metadata_entry_data={"out": "xml", "timeout": 255}
)
print(testcase_gen_metadata)
