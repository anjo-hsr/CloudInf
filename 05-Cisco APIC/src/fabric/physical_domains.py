from src.helpers.helper_json_files import json_file_to_post_requests


def create_physical_domains(connection):
    file_path = "./_json_files/fabric/physical_domains.json"
    json_file_to_post_requests(connection, file_path, "physical_domains_array", "physDomP")
