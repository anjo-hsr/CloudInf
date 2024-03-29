import collections

from src.helpers.connection_handler import is_netconf_socket_open
from src.helpers.constants import connection_parameters, clean_connection_parameters, methods, filter_xml_files
from src.helpers.parameter_handler import is_a_parameter_none
from src.helpers.terminal_handler import get_error_string, get_bold_string, get_info_string


def get_connection():
    parameters = connection_parameters.copy()
    print("\nThe default connection setup uses the PE switch " + get_bold_string(parameters["host"]) + ".")
    choice = input("Would you like to setup your own connection: [N/y]\t") or "N"
    if choice == "y" or not is_netconf_socket_open(parameters.get("host"), parameters.get("port")):

        parameters = clean_connection_parameters.copy()

        while is_a_parameter_none(parameters):
            parameters["host"] = input("Please enter the " + get_info_string("host") + ":\t") or None
            parameters["port"] = input("Please enter the " + get_info_string("port") + ":\t") or None
            parameters["username"] = input("Please enter the " + get_info_string("username") + ":\t") or None
            parameters["password"] = input("Please enter the " + get_info_string("password") + ":\t") or None

            if not is_netconf_socket_open(parameters.get("host"), parameters.get("port")):
                parameters = clean_connection_parameters.copy()

    return parameters


def display_methods():
    for key in methods:
        print("- " + key)
    return input("What would you like to do?: \t") or None


def get_filter():
    filter_xml = select_from_dict(filter_xml_files, " filter", "")

    Map = collections.namedtuple('Map', ['key', 'value'])
    key = filter_xml.key
    value = None

    if filter_xml.key != "exit":
        with open("./files/" + filter_xml.value) as xml_file:
            value = xml_file.read()

    return Map(key, value)


def select_from_dict(selected_dict, selection_type, default=""):
    print("\n")
    value = None
    key = None
    while value is None:
        try:
            for key in selected_dict.keys():
                print("- " + key)
            key = input("Please select a" + selection_type + " from the list above: [" + default + "]\t") or default
            value = selected_dict[key]
        except KeyError:
            print("\n" + get_error_string("Please try again with these keys:"))
            value = None

    Map = collections.namedtuple('Map', ['key', 'value'])
    return Map(key, value)
