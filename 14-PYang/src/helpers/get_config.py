def get_main_config(m):
    return m.get_config(source="running")


def get_filtered_config(m, xml_filter):
    return m.get_config(source="running", filter=xml_filter)
