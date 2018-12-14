def get_main_config(source, m):
    return m.get_config(source=source)


def get_filtered_config(source, m, xml_filter):
    return m.get_config(source=source, filter=xml_filter)
