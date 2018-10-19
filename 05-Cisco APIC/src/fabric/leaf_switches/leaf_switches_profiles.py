from src.helpers.helper_json_files import json_file_to_post_requests


def generate_leaf_switches_profiles(connection):
    file_path = "./_json_files/fabric/leaf_switches/profiles.json"
    json_file_to_post_requests(connection, file_path, "application_epg_array", "fvAEPg")