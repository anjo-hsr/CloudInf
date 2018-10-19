from src.helpers.helper_json_files import json_file_to_post_requests


def attachable_access_entity_profiles(connection):
    file_path = "./_json_files/fabric/attachable_access_entity_profiles.json"
    json_file_to_post_requests(connection, file_path, "infrastructure_array", "infraInfra")
