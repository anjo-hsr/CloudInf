import collections

from src.helpers.constants import connection_parameters, datastores, xml_filters, add_xml_files, delete_xml_files, \
    vrf_add_parameters, vrf_delete_parameters


def get_connection():
    parameters = connection_parameters
    print("The default connection setup uses Ciscos sandbox infrastructure")
    choice = input("Would you like to setup your own connection: [N/y]\t") or "N"
    if choice == "y":
        parameters["host"] = input(
            "Please enter the hostname or ip: [ios-xe-mgmt.cisco.com]\t") or "ios-xe-mgmt.cisco.com"
        parameters["port"] = input("Please enter the port number: [10000]\t") or 10000
        parameters["username"] = input("Please enter the username: [root]\t") or "root"
        parameters["password"] = input("Please enter the password: [D_Vay!_10&]\t") or "D_Vay!_10&"

    return dict([
        ("host", parameters["host"]),
        ("port", parameters["port"]),
        ("username", parameters["username"]),
        ("password", parameters["password"])
    ])


def get_datastore():
    return select_from_dict(datastores, " datastore", "running").value


def get_filter():
    return select_from_dict(xml_filters, " filter").value


def is_a_parameter_none(vrf_parameters):
    start_boolean = True
    for key in vrf_parameters.keys():
        start_boolean = start_boolean and (vrf_parameters[key] is None)
    return start_boolean


def get_vrf_add_xml(filename):
    parameters = vrf_add_parameters

    while is_a_parameter_none(parameters):
        parameters["name"] = input("Please input the name for the new vrf: \t") or None
        parameters["rd_address"] = input("Please input the address of the rd: \t") or None
        parameters["rd_port"] = input("Please input the port of the rd: \t") or None
        parameters["asn_address"] = input("Please input the asn address: \t") or None
        parameters["asn_port"] = input("Please input the asn port: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_vrf_delete_xml(filename):
    parameters = vrf_delete_parameters

    while is_a_parameter_none(parameters):
        parameters["name"] = input("Please input the name for the new vrf: \t") or None

    return replace_variables_in_file(filename, parameters)


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
