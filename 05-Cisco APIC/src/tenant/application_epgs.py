from src.helpers.helper_json_files import json_file_to_data
from src.helpers.helper_request_generator import get_post_address, make_post_request


# Copy paste have to be done because over each new epg the static ports have to be set.
def create_application_epgs(connection):
    file_path = "./_json_files/tenant/application_profiles/application_epgs/application_epgs.json"

    json_array_name = "application_epg_array"
    json_main_attribute = "fvAEPg"

    data = json_file_to_data(file_path)

    for element in data[json_array_name]:
        application_epg_dn = element[json_main_attribute]["attributes"]["dn"]
        __create_static_ports(connection, application_epg_dn)


# The POST must be done to each epg object, that's why the epg_dn is required
def __create_static_ports(connection, epg_dn):
    file_path = "./_json_files/tenant/application_profiles/application_epgs/static_ports.json"

    data = json_file_to_data(file_path)

    # Check for epg must be done to prevent that a epg is mapped to both ports
    if "green_epg" in epg_dn:
        post_address = get_post_address(connection.get_https_address(), epg_dn)
        make_post_request(post_address, connection, data["static_port_green"])

    if "red_epg" in epg_dn:
        post_address = get_post_address(connection.get_https_address(), epg_dn)
        make_post_request(post_address, connection, data["static_port_red"])
