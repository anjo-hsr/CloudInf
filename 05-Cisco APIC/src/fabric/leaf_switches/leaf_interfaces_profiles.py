from src.helpers.helper_json_files import json_file_to_post_requests


def create_leaf_interfaces_profiles(connection):
    file_path = "./_json_files/fabric/leaf_interfaces_profiles.json"
    json_file_to_post_requests(connection, file_path, "leaf_interfaces_profile_array", "infraAccPortP")
