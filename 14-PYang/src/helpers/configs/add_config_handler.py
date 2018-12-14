from src.helpers.constants import bgp_add_parameters, vlan_add_parameters, vrf_add_parameters, add_xml_files
from src.helpers.input_handler import is_a_parameter_none, replace_variables_in_file, select_from_dict


def get_vrf_add_xml(filename):
    parameters = vrf_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input("Please configs the name for the new vrf: \t") or None
        parameters["rd_address"] = input("Please configs the address of the rd: \t") or None
        parameters["rd_port"] = input("Please configs the port of the rd: \t") or None
        parameters["asn_address"] = input("Please configs the asn address: \t") or None
        parameters["asn_port"] = input("Please configs the asn port: \t") or None
        parameters["as_id"] = input("Please configs the as id: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_bgp_add_xml(filename):
    parameters = bgp_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["as_id"] = input("Please configs the local as id from the router: \t") or None
        parameters["remote_id"] = input("Please configs the remote id from the other bgp router: \t") or None
        parameters["remote_as"] = input("Please configs the remote as from the other bgp router: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_vlan_add_xml(filename):
    parameters = vlan_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["vlan_id"] = input("Please configs the id of the new vlan: \t") or None
        parameters["vrf_name"] = input("Please configs the vrf name which will forward the new vlan: \t") or ""

    return replace_variables_in_file(filename, parameters)


def get_add_configs():
    config_file = select_from_dict(add_xml_files, "n add config file")

    if config_file.key == "vrf":
        return get_vrf_add_xml(config_file.value)

    if config_file.key == "bgp":
        return get_bgp_add_xml(config_file.value)

    if config_file.key == "vlan":
        return get_vlan_add_xml(config_file.value)

    exit(1)
