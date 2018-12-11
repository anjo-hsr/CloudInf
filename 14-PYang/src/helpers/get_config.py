def get_config(source, netconf_connection, xml_string):
    source = "running"
    return netconf_connection.get_config(source=source, filter=xml_string)
