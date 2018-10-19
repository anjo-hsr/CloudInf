from src.helpers.helper_json_files import json_file_to_post_requests


def create_leaf_profiles(connection):
    file_path = "./_json_files/fabric/leaf_profiles.json"
    json_file_to_post_requests(connection, file_path, "leaf_profile_array", "infraNodeP")
