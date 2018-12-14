def get_main_config(m, datastore):
    return m.get_config(source=datastore)


def get_filtered_config(m, datastore, xml_filter):
    return m.get_config(source=datastore, filter=xml_filter)
