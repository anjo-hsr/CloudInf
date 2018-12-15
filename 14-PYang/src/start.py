import atexit
import os

from src.helpers.configs.edit_config import add_xml_config, delete_xml_config
from src.helpers.configs.print_config import print_filtered_config, print_all
from src.helpers.connection_handler import check_connection, check_and_close_connection, generate_connection
from src.helpers.get_config import get_main_config
from src.helpers.input_handler import get_connection, display_methods


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


connection_parameters = get_connection()
m = generate_connection(connection_parameters)
atexit.register(check_and_close_connection, m)

check_connection(m)

repeat = True
while repeat:
    cls()
    repeat = False

    print("Connected with " + connection_parameters["host"] + ":" + str(connection_parameters["port"]) + "\n")
    chosen_method = display_methods()
    if chosen_method == "displayAll":
        main_config = get_main_config(m)
        print_all(main_config)

    if chosen_method == "filter":
        print_filtered_config(m)

    if chosen_method == "add":
        add_xml_config(m)

    if chosen_method == "delete":
        delete_xml_config(m)

    if chosen_method == "changeDevice":
        connection_parameters = get_connection()
        m = generate_connection(connection_parameters)
        repeat = True

    if chosen_method == "exit":
        break

    if not repeat:
        repeat = (input("Would you like to continue? [Y/n]") or "Y") == "Y"

check_and_close_connection(m)
exit()
