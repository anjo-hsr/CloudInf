import collections

from src.helpers.color_handler import get_background_colored_string
from src.helpers.constants import delete_xml_files, bgp_delete_parameters, vlan_delete_parameters, vrf_delete_parameters
from src.helpers.input_handler import is_a_parameter_none, replace_variables_in_file, select_from_dict


def __get_bgp_delete_xml(filename):
    parameters = bgp_delete_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["as_id"] = input(
            "Please enter the current used bgp " + get_background_colored_string("as id") + ": \t") or None
        parameters["remote_id"] = input(
            "Please enter the " + get_background_colored_string("remote id") + ": \t") or None

    return replace_variables_in_file(filename, parameters)


def __get_vrf_delete_xml(filename):
    parameters = vrf_delete_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input(
            "Please enter the " + get_background_colored_string("name from the vrf") + " to delete: \t") or None
        parameters["as_id"] = input(
            "Please enter the current used " + get_background_colored_string("bgp as id") + " from the vrf: \t") or None
        parameters["vlan_id"] = input(
            "Please enter the current used " + get_background_colored_string("vlan id") + ": \t") or None

    return replace_variables_in_file(filename, parameters)


def __get_vlan_delete_xml(filename):
    parameters = vlan_delete_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["vlan_id"] = input("Please enter the " + get_background_colored_string("vlan id") + " to delete: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_delete_configs():
    config_file = select_from_dict(delete_xml_files, " delete config file")
    Map = collections.namedtuple('Map', ['key', 'xml'])

    if config_file.key == "bgp":
        return Map("bgp", __get_bgp_delete_xml(config_file.value))

    if config_file.key == "vlan":
        return Map("vlan", __get_vlan_delete_xml(config_file.value))

    if config_file.key == "vrf":
        return Map("vrf", __get_vrf_delete_xml(config_file.value))


def get_bgp_neighbor_delete_config():
    Map = collections.namedtuple('Map', ['key', 'xml'])
    return Map("bgp", __get_bgp_delete_xml(delete_xml_files["bgp"]))
