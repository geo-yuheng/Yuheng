from typing import Optional, Union, List

query_template = "<metadata_part>\n<condition_part>\n<output_part>"


def gen_metadata(**kwargs) -> Optional[str]:
    buffer = ""

    def wrap_metadata(key: str, value: Union[str, int, float]) -> str:
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return f"[{key}:{value}]"

    if kwargs.get("metadata_entry_data"):
        for metadata_entry_key in kwargs.get("metadata_entry_data"):
            metadata_entry_value = kwargs.get("metadata_entry_data").get(
                metadata_entry_key, ""
            )
            possible_key = [
                "out",
                "timeout",
                "maxsize",
                "bbox",
                "date",
                "diff",
            ]
            possible_value_for_out_key = [
                "xml",
                "json",
                "csv",
                "custom",
                "popup",
            ]
            if metadata_entry_key == "out" and metadata_entry_value in [
                "xml",
                "json",
            ]:
                buffer += wrap_metadata(
                    metadata_entry_key, metadata_entry_value
                )
                # There should be a lint about final part after output format detected, I guess, such as geom/meta/body.
            elif metadata_entry_key == "out" and metadata_entry_value == "csv":

                def gen_csv_key_list():
                    def gen_magic_key(**kwargs):
                        buffer = ""
                        if kwargs.get("type"):
                            buffer += "::type"
                        if kwargs.get("id"):
                            buffer += "::id"
                        if kwargs.get("type_str"):
                            buffer += '::"type"'
                        if kwargs.get("id_str"):
                            buffer += '::"id"'
                        return buffer

                    return gen_magic_key() + ",".join(
                        ['"' + i + '"' for i in query_key_list]
                    )

                csv_argument = kwargs.get("csv_argument")
                query_key_list: List[str] = csv_argument.get(
                    "query_key_list", []
                )
                metadata_csv_content = gen_csv_key_list()
                if csv_argument.get("explicit_declare_header", None) != None:
                    metadata_csv_content += (
                        ";"
                        + str(
                            csv_argument.get("explicit_declare_header")
                        ).lower()
                    )
                if csv_argument.get("delimiter"):
                    metadata_csv_content += (
                        ";" + f"\"{csv_argument.get('delimiter')}\""
                    )
                buffer += f"[out:csv({metadata_csv_content})]"
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


print(
    gen_metadata(
        metadata_entry_data={"out": "xml", "timeout": 255, "bbox": "earth"}
    )
)
print(
    gen_metadata(
        metadata_entry_data={
            "out": "csv",
            "timeout": 255,
        },
        csv_argument={
            "query_key_list": ["amenity", "addr:city", "admin_level"],
            "explicit_declare_header": True,
            "delimiter": "|",
        },
    )
)
