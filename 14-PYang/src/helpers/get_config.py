def get_main_config(source, m):
    return m.get_config(source=source)


def get_filtered_config(m, datastore, xml_filter):
    return m.get_config(source=datastore, filter=xml_filter)
