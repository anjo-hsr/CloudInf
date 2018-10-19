from src.helpers.helper_json_files import json_file_to_post_requests


def generate_bridge_domains(connection):
    file_path = "./_json_files/tenant/bridge_domains.json"
    json_file_to_post_requests(connection, file_path, "bridge_domain_array", "fvBD")
