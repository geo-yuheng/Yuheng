query_template = "<metadata_part>\n<condition_part>\n<output_part>"


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
