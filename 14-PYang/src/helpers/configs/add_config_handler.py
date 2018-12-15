from src.helpers.color_handler import get_background_colored_string
from src.helpers.constants import bgp_add_parameters, vlan_add_parameters, vrf_add_parameters, add_xml_files
from src.helpers.input_handler import is_a_parameter_none, replace_variables_in_file, select_from_dict


def get_vrf_add_xml(filename):
    parameters = vrf_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input(
            "Please enter the " + get_background_colored_string("name from the vrf") + ": \t") or None
        parameters["rd_address"] = input(
            "Please enter the " + get_background_colored_string("address of the rd") + ": \t") or None
        parameters["rd_port"] = input(
            "Please enter the " + get_background_colored_string("port of the rd") + ": \t") or None
        parameters["asn_address"] = input(
            "Please enter the " + get_background_colored_string("asn address") + ": \t") or None
        parameters["asn_port"] = input(
            "Please enter the " + get_background_colored_string("asn port") + ": \t") or None
        parameters["as_id"] = input(
            "Please enter the " + get_background_colored_string("as id") + ": \t") or None

    return replace_variables_in_file(filename, parameters)


def get_bgp_add_xml(filename):
    parameters = bgp_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["as_id"] = input(
            "Please enter the local " + get_background_colored_string("as id") + " from the router: \t") or None
        parameters["remote_id"] = input(
            "Please enter the " + get_background_colored_string("remote id") + " from the other bgp router: \t") or None
        parameters["remote_as"] = input(
            "Please enter the " + get_background_colored_string("remote as") + " from the other bgp router: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_vlan_add_xml(filename):
    parameters = vlan_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["vlan_id"] = input(
            "Please enter the  " + get_background_colored_string("vlan id") + " from the vlan: \t") or None
        parameters["vrf_name"] = input(
            "Please enter the " + get_background_colored_string("vrf name") + ": \t") or None

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
