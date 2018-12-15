import collections

from src.helpers.constants import connection_parameters, clean_connection_parameters, methods
from src.helpers.filters import xml_filters
from src.helpers.terminal_handler import get_error_string, get_bold_string, get_info_string


def get_connection():
    parameters = connection_parameters.copy()
    print("The default connection setup uses the PE switch " + get_bold_string(parameters["host"]) + ".")
    choice = input("Would you like to setup your own connection: [N/y]\t") or "N"
    if choice == "y":

        parameters = clean_connection_parameters.copy()

        while is_a_parameter_none(parameters):
            parameters["host"] = input("Please enter the " + get_info_string("host") + ":\t") or None
            parameters["port"] = input("Please enter the " + get_info_string("port") + ":\t") or None
            parameters["username"] = input("Please enter the " + get_info_string("username") + ":\t") or None
            parameters["password"] = input("Please enter the " + get_info_string("password") + ":\t") or None

    return parameters


def display_methods():
    for key in methods:
        print("- " + key)
    return input("What would you like to do?: \t") or None


def is_a_parameter_none(vrf_parameters):
    start_boolean = False
    for key in vrf_parameters.keys():
        start_boolean = start_boolean or (vrf_parameters[key] is None)
    return start_boolean


def replace_variables_in_file(filename, parameters):
    with open("./files/" + filename) as xml_file:
        imported_xml_file = xml_file.read()
        for key in parameters.keys():
            imported_xml_file = imported_xml_file.replace("{{" + str(key) + "}}", parameters[key])
    return imported_xml_file


def get_filter():
    filter_xml = select_from_dict(xml_filters, " filter", "")
    if filter_xml.key != "exit":
        return filter_xml

    return None


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
