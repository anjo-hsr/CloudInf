from src.helpers.helper_json_files import json_file_to_post_requests


def generate_default_contracts(connection):
    file_path = "./_json_files/tenant/contracts/contracts.json"
    json_file_to_post_requests(connection, file_path, "contract_array", "vzBrCP")