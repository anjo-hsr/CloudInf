import xml.dom.minidom as xml

from src.helpers.connection_handler import check_connection


def print_and_close(m, config):
    print_config(config)
    m.close_session()
    check_connection(m)


def print_config(config):
    print(xml.parseString(config.xml).toprettyxml())
