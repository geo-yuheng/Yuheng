from typing import Optional, Union

query_template = "<metadata_part>\n<condition_part>\n<output_part>"


def gen_metadata(**kwargs) -> Optional[str]:
    buffer = ""

    def wrap_metadata(key: str, value: Union[str, int, float]) -> str:
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return f"[{key}:{value}]"

    if kwargs.get("metadata_entry_data"):
        for metadata_entry in kwargs.get("metadata_entry_data"):
            # print(kwargs.get("metadata_entry_data").get(metadata_entry))
            buffer += wrap_metadata(
                metadata_entry,
                kwargs.get("metadata_entry_data").get(metadata_entry, ""),
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
