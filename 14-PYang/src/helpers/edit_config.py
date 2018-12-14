from src.helpers.input_handler import get_add_configs, get_delete_configs, get_filter
from src.helpers.get_config import get_filtered_config
from src.helpers.print_config import print_config


def add_xml_config(m, datastore):
    add_config_xml = get_add_configs()
    alter_config(m, datastore, add_config_xml)
    xml_filter = get_filter()
    config = get_filtered_config(datastore, m, xml_filter)
    print_config(config)


def delete_xml_config(m, datastore):
    delete_config_xml = get_delete_configs()
    alter_config(m, datastore, delete_config_xml)
    xml_filter = get_filter()
    config = get_filtered_config(datastore, m, xml_filter)
    print_config(config)


def alter_config(m, datastore, alter_config_xml):
    with m.locked(target=datastore):
        res = m.edit_config(config=alter_config_xml, target=datastore)

    print(res)
