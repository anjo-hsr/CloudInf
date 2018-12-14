from src.helpers.constants import delete_xml_files, vrf_delete_parameters
from src.helpers.input_handler import is_a_parameter_none, replace_variables_in_file, select_from_dict


def get_vrf_delete_xml(filename):
    parameters = vrf_delete_parameters.copy()

    while is_a_parameter_none(parameters):
        parameters["name"] = input("Please configs the name from the vrf to delete: \t") or None
        parameters["as_id"] = input("Please configs the current used bgp as id from the vrf: \t") or None
        parameters["vlan_id"] = input("Please configs the current used vlan id: \t") or None

    return replace_variables_in_file(filename, parameters)


def get_delete_configs():
    config_file = select_from_dict(delete_xml_files, " delete config file")

    if config_file.key == "bgp":
        return get_vrf_delete_xml(config_file.value)

    if config_file.key == "vrf":
        return get_vrf_delete_xml(config_file.value)
