import collections

from src.helpers.filters import xml_filters
from src.helpers.constants import connection_parameters, datastores, add_xml_files, delete_xml_files, \
    bgp_add_parameters, vlan_add_parameters, vrf_add_parameters, vrf_delete_parameters, clean_connection_parameters, \
    methods


def get_connection():
    parameters = connection_parameters.copy()
    print("The default connection setup uses Ciscos sandbox infrastructure")
    choice = input("Would you like to setup your own connection: [N/y]\t") or "N"
    if choice == "y":

        parameters = clean_connection_parameters.copy()

        while is_a_parameter_none(parameters):
            for key in parameters.keys():
                parameters[key] = input("Please enter the" + key + ":\t")

    return parameters


def display_methods():
    print("\n\n")
    for key in methods:
        print("- " + key)
    return input("What would you like to do?: \t") or None


def get_vrf_add_xml(filename):
    parameters = vrf_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input("Please input the name for the new vrf: \t") or None
        parameters["rd_address"] = input("Please input the address of the rd: \t") or None
        parameters["rd_port"] = input("Please input the port of the rd: \t") or None
        parameters["asn_address"] = input("Please input the asn address: \t") or None
        parameters["asn_port"] = input("Please input the asn port: \t") or None
        parameters["as_id"] = input("Please input the as id: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_bgp_add_xml(filename):
    parameters = bgp_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["as_id"] = input("Please input the local as id from the router: \t") or None
        parameters["remote_id"] = input("Please input the remote id from the other bgp router: \t") or None
        parameters["remote_as"] = input("Please input the remote as from the other bgp router: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_vrf_delete_xml(filename):
    parameters = vrf_delete_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input("Please input the name from the vrf to delete: \t") or None
        parameters["as_id"] = input("Please input the current used bgp as id from the vrf: \t") or None
        parameters["vlan_id"] = input("Please input the current used vlan id: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_vlan_add_xml(filename):
    parameters = vlan_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["vlan_id"] = input("Please input the id of the new vlan: \t") or None
        parameters["vrf_name"] = input("Please input the vrf name which will forward the new vlan: \t") or ""

    return replace_variables_in_file(filename, parameters)


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


def get_add_configs():
    config_file = select_from_dict(add_xml_files, "n add config file")

    if config_file.key == "vrf":
        return get_vrf_add_xml(config_file.value)

    if config_file.key == "bgp":
        return get_bgp_add_xml(config_file.value)

    if config_file.key == "vlan":
        return get_vlan_add_xml(config_file.value)

    exit(1)


def get_datastore():
    return select_from_dict(datastores, " datastore", "running").value


def get_filter():
    filter_xml = select_from_dict(xml_filters, " filter", "")
    if filter_xml.key != "exit":
        return filter_xml

    return None


def get_delete_configs():
    config_file = select_from_dict(delete_xml_files, " delete config file")

    if config_file.key == "vrf":
        return get_vrf_delete_xml(config_file.value)


def select_from_dict(selected_dict, selection_type, default=""):
    print("\n\n")
    value = None
    key = None
    while value is None:
        try:
            for key in selected_dict.keys():
                print("- " + key)
            key = input("Please select a" + selection_type + " from the list above: [" + default + "]\t") or default
            value = selected_dict[key]
        except KeyError:
            print("\nPlease try again with these keys:")
            value = None

    Map = collections.namedtuple('Map', ['key', 'value'])
    return Map(key, value)
