import collections

from src.helpers.constants import bgp_add_parameters, vlan_add_parameters, vrf_add_parameters, add_xml_files
from src.helpers.input_handler import is_a_parameter_none, replace_variables_in_file, select_from_dict
from src.helpers.terminal_handler import get_info_string


def __get_vrf_add_xml(filename):
    parameters = vrf_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input(
            "Please enter the " + get_info_string("name from the vrf") + ": \t") or None
        parameters["rd_address"] = input(
            "Please enter the " + get_info_string("address of the rd") + ": \t") or None
        parameters["rd_port"] = input(
            "Please enter the " + get_info_string("port of the rd") + ": \t") or None
        parameters["asn_address"] = input(
            "Please enter the " + get_info_string("asn address") + ": \t") or None
        parameters["asn_port"] = input(
            "Please enter the " + get_info_string("asn port") + ": \t") or None
        parameters["as_id"] = input(
            "Please enter the " + get_info_string("as id") + ": \t") or None

    return replace_variables_in_file(filename, parameters)


def __get_bgp_add_xml(filename):
    parameters = bgp_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["as_id"] = input(
            "Please enter the " + get_info_string("local as id") + " from the router: \t") or None
        parameters["remote_id"] = input(
            "Please enter the " + get_info_string("remote id") + " from the other bgp router: \t") or None
        parameters["remote_as"] = input(
            "Please enter the " + get_info_string("remote as id") + " from the other bgp router: \t") or None

    return replace_variables_in_file(filename, parameters)


def __get_vlan_add_xml(filename):
    parameters = vlan_add_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["vlan_id"] = input(
            "Please enter the  " + get_info_string("vlan id") + " from the vlan: \t") or None
        parameters["vrf_name"] = input(
            "Please enter the " + get_info_string("vrf name") + ": \t") or None

    return replace_variables_in_file(filename, parameters)


def get_add_configs():
    config_file = select_from_dict(add_xml_files, "n add config file")
    Map = collections.namedtuple('Map', ['key', 'xml'])

    if config_file.key == "bgp":
        return Map("bgp", __get_bgp_add_xml(config_file.value))

    if config_file.key == "vlan":
        return Map("vlan", __get_vlan_add_xml(config_file.value))

    if config_file.key == "vrf":
        return Map("vrf", __get_vrf_add_xml(config_file.value))

    return Map(None, None)


def get_bgp_neighbor_add_config():
    Map = collections.namedtuple('Map', ['key', 'xml'])
    return Map("bgp", __get_bgp_add_xml(add_xml_files["bgp"]))
