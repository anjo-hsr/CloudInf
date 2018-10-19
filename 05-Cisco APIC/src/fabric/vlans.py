from src.helpers.helper_json_files import json_file_to_post_requests


def create_vlans(connection):
    file_path = "./_json_files/fabric/vlans.json"
    json_file_to_post_requests(connection, file_path, "vlans_array", "fvnsVlanInstP")
