from src.helpers.helper_json_files import json_file_to_data, json_file_to_post_requests
from src.helpers.helper_request_generator import get_post_address, make_post_request


# Copy paste have to be done because over each new epg the static ports have to be set.
def create_application_epgs(connection):
    file_path = "./_json_files/tenant/application_profiles/application_epgs/application_epgs.json"

    json_array_name = "application_epg_array"
    json_main_attribute = "fvAEPg"

    data = json_file_to_data(file_path)

    for element in data[json_array_name]:
        application_epg_dn = element[json_main_attribute]["attributes"]["dn"]
        post_address = get_post_address(connection.get_https_address(), application_epg_dn)
        make_post_request(post_address, connection, element)
        __create_static_ports(connection, application_epg_dn)


# The POST must be done to each epg object thats why the epg_dn is required
def __create_static_ports(connection, epg_dn):
    print("\n\n*********************\nStart of static ports\n" + epg_dn + "*****************\n\n")

    file_path = "./_json_files/tenant/application_profiles/application_epgs/static_ports.json"

    json_array_name = "static_port_array"
    data = json_file_to_data(file_path)

    for element in data[json_array_name]:
        post_address = get_post_address(connection.get_https_address(), epg_dn)
        make_post_request(post_address, connection, element)
