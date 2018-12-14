import os

from src.helpers.connection_handler import check_connection, generate_connection

from src.helpers.input_handler import get_connection, get_datastore, display_methods
from src.helpers.configs.edit_config import add_xml_config, delete_xml_config
from src.helpers.configs.print_config import print_filtered_config, print_all
from src.helpers.get_config import get_main_config


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


m = generate_connection(get_connection())
check_connection(m)
datastore = get_datastore()

repeat = True
while repeat:
    cls()
    chosen_method = display_methods()
    if chosen_method == "displayAll":
        main_config = get_main_config(m, datastore)
        print_all(main_config)

    if chosen_method == "filter":
        print_filtered_config(m, datastore)
    if chosen_method == "add":
        add_xml_config(m, datastore)
    if chosen_method == "delete":
        delete_xml_config(m, datastore)
    if chosen_method == "exit":
        break

    repeat = (input("Would you like to repeat? [Y/n]") or "Y") == "Y"

m.close_session()
exit()
