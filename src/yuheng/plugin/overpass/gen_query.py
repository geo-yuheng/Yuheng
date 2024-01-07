query_template = "<metadata_part>\n<condition_part>\n<output_part>"


def gen_query():
    return (
        query_template.replace("<metadata_part>", gen_metadata())
        .replace("<condition_part>", gen_condition())
        .replace("<output_part>", gen_output())
    )
