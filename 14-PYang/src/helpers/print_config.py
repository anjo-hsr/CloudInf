import xml.dom.minidom


def print_config(config):
    print(xml.dom.minidom.parseString(config.xml).toprettyxml())
