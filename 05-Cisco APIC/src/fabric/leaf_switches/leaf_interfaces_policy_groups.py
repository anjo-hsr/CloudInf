from src.helpers.helper_json_files import json_file_to_post_requests


def __create_leaf_access_ports(connection):
    file_path = "./_json_files/fabric/leaf_access_ports.json"
    json_file_to_post_requests(connection, file_path, "leaf_access_port_array", "infraAccPortGrp")


def __create_vpc_interfaces(connection):
    file_path = "./_json_files/fabric/vpc_interfaces.json"
    json_file_to_post_requests(connection, file_path, "vpc_interface_array", "infraAccBndlGrp")


def create_policy_groups(connection):
    __create_leaf_access_ports(connection)
    __create_vpc_interfaces(connection)
