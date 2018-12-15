from src.helpers.configs.add_config_handler import get_add_configs
from src.helpers.configs.delete_config_handler import get_delete_configs, get_bgp_neighbor_delete_config

from src.helpers.connection_handler import generate_connection
from src.helpers.input_handler import get_connection
from src.helpers.terminal_handler import get_info_string, get_error_string, get_successful_string


def add_xml_config(m):
    add_config_xml = get_add_configs()
    alter_config(m, add_config_xml)


def delete_xml_config(m):
    delete_config = get_delete_configs()
    alter_config(m, delete_config.xml)

    if delete_config.key == "bgp":
        print("\nYou have deleted the bgp neighborship from a router. Now you proceed with deleting the neighborship "
              "from the neighbor by " + get_info_string("switching the script to another router") + ".")
        delete_now = input("Would you like to do that now. [Y/n]")

        if delete_now == "Y":
            print(get_info_string("OK, please enter the new connection parameters to continue:"))
            connection_parameters = get_connection()
            m2 = generate_connection(connection_parameters)

            print(get_info_string("Now enter the parameters to delete the remote bgp connection:"))
            delete_config = get_bgp_neighbor_delete_config()

            alter_config(m2, delete_config.xml)
            print(get_info_string("Closing connection from external router"))
            m2.close_session()


def alter_config(m, alter_config_xml):
    # Thanks to Carl Moberg from Cisco:
    #  - code: https://github.com/cmoberg/netconf-yang-training/blob/master/example-csr1000v/08_cmd-add-mpls-lsp-full.py
    #  - slided: https://github.com/cmoberg/netconf-yang-training/tree/master/slides

    # Check if requirements are done. Otherwise enable candidate-datastore
    assert (":candidate" in m.server_capabilities)
    assert (":validate" in m.server_capabilities)

    # This is best practice to prevent simultaneously edit of the candidate storage.
    with m.locked(target="candidate"):
        m.discard_changes()
        m.edit_config(config=alter_config_xml, target="candidate")
        m.validate()
        res = m.commit()

        if "ok" in res.xml:
            print("\n" + get_successful_string("Sucessfully altered the config"))
        else:
            print("\n" + get_error_string("Error occured with the altering process"))
