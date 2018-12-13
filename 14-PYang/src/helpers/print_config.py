import xml.dom.minidom as xml


def print_config(config):
    print(xml.parseString(config.xml).toprettyxml())
