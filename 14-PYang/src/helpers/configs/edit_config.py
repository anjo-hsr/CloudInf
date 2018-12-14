from src.helpers.configs.add_config_handler import get_add_configs
from src.helpers.configs.delete_config_handler import get_delete_configs


def add_xml_config(m, datastore):
    add_config_xml = get_add_configs()
    alter_config(m, datastore, add_config_xml)


def delete_xml_config(m, datastore):
    delete_config_xml = get_delete_configs()
    alter_config(m, datastore, delete_config_xml)


def alter_config(m, datastore, alter_config_xml):
    with m.locked(target=datastore):
        # try:
        res = m.edit_config(config=alter_config_xml, target=datastore)
        if "ok" in res.xml:
            print("Sucessfully altered the config")
        else:
            print("Error occured with the altering process")
        # except:
        #    print("Invalid arguments provided or service not deleted from other interfaces")

    print("\n\n")
