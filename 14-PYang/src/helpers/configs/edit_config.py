from src.helpers.configs.add_config_handler import get_add_configs
from src.helpers.configs.delete_config_handler import get_delete_configs


def add_xml_config(m):
    add_config_xml = get_add_configs()
    alter_config(m, add_config_xml)


def delete_xml_config(m):
    delete_config_xml = get_delete_configs()
    alter_config(m, delete_config_xml)


def alter_config(m, alter_config_xml):
    # Thanks to Carl Moberg from Cisco:
    #   - code: https://github.com/cmoberg/netconf-yang-training/blob/master/example-csr1000v/08_cmd-add-mpls-lsp-full.py
    #   - slided: https://github.com/cmoberg/netconf-yang-training/tree/master/slides

    try:
        assert (":candidate" in m.server_capabilities)
        assert (":validate" in m.server_capabilities)
        with m.locked(target="candidate"):
            m.discard_changes()
            m.edit_config(config=alter_config_xml, target="candidate")
            m.validate()
            res = m.commit()

            if "ok" in res.xml:
                print("\nSucessfully altered the config")
            else:
                print("Error occured with the altering process")

    except Exception as e:
        print(e)
        print("Invalid arguments provided or service not deleted from other interfaces")

    finally:
        print("\n\n")
