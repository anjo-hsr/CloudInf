import xmltodict


def add_filter(config, filter):
    config_dict = xmltodict.parse(config.xml)
    config_dict["rpc-reply"]["data"] = xmltodict.parse(filter)
    return xmltodict.unparse(config_dict)
