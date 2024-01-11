from typing import Optional, Union, List

query_template = "<metadata_part>\n<condition_part>\n<output_part>"


def gen_metadata(**kwargs) -> Optional[str]:
    buffer = ""

    def wrap_metadata(key: str, value: Union[str, int, float]) -> str:
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return f"[{key}:{value}]"

    query_key_list: List[str] = kwargs.get("query_key_list", [])
    metadata_csv_template = "[out:csv({{content}})];"
    # #
    # ::type,
    # ::id,{{key_list}};
    # true; "|"

    def gen_magic_key(**kwargs):
        buffer=""
        if kwargs.get("type"):
            buffer+="::type"
        if kwargs.get("id"):
            buffer+="::id"
        if kwargs.get("type_str"):
            buffer+="::\"type\""
        if kwargs.get("id_str"):
            buffer+="::\"id\""
        return buffer

    def gen_csv_key_list ():
        return gen_magic_key() + ",".join(
        ['"' + i + '"' for i in query_key_list]
    )

    if kwargs.get("metadata_entry_data"):
        for metadata_entry_key in kwargs.get("metadata_entry_data"):
            metadata_entry_value = kwargs.get("metadata_entry_data").get(
                metadata_entry_key, ""
            )
            # possible key:
            # * out
            # * timeout
            # * maxsize
            # * bbox
            # * date
            # * diff
            # possible value for "out" key:
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
                buffer+=
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
