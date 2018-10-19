from src.helpers.helper_json_files import json_file_to_data, json_file_to_post_requests
from src.helpers.helper_request_generator import get_post_address, make_post_request
from src.tenant.bind_contracts import bind_contracts


def __generate_empty_application_profiles(connection):
    file_path = "./_json_files/tenant/application_profiles/empty_application_profiles.json"
    json_file_to_post_requests(connection, file_path, "application_profile_array", "fvAp")


def __generate_application_epgs(connection):
    application_epgs = json_file_to_data("./_json_files/tenant/application_profiles/application_epgs/application_epgs.json")

    for application_epg in application_epgs['application_epg_array']:
        application_epg_dn = application_epg["fvAEPg"]["attributes"]["dn"]
        post_address = get_post_address(connection.get_https_address(), application_epg_dn)
        make_post_request(post_address, connection, application_epg)
        bind_contracts(connection, application_epg_dn)


def generate_application_profiles(connection):
    __generate_empty_application_profiles(connection)
    __generate_application_epgs(connection)
