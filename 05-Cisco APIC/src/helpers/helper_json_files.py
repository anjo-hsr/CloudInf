from src.helpers.helper_request_generator import get_post_address, make_post_request

import json


def generate_json_from_file(file):
    return json.load(file)


def json_file_to_data(file_path):
    with open(file_path) as json_file:
        data = generate_json_from_file(json_file)

    return data


def json_file_to_post_requests(connection, file_path, json_array_name, json_main_attribute):
    json_data = json_file_to_data(file_path)
    for element in json_data[json_array_name]:
        json_element_to_post_requests(connection, element, json_main_attribute)


def json_element_to_post_requests(connection, json_element, json_main_attribute):
    application_epg_dn = json_element[json_main_attribute]["attributes"]["dn"]
    post_address = get_post_address(connection.get_https_address(), application_epg_dn)
    make_post_request(post_address, connection, json_element)
