from src.helpers.helper_json_files import json_file_to_post_requests
from src.helpers.helper_json_files import generate_json_from_file, make_post_request


def create_physical_domains(connection):
    file_path = "./_json_files/fabric/physical_domains.json"
    json_file_to_post_requests(connection, file_path, "physical_domain_array", "physDomP")


def bind_physical_domain(connection, post_address):
    with open('./_json_files/tenant/application_profiles/physical_domains.json') as contracts_between_egps_file:
        physical_domains = generate_json_from_file(contracts_between_egps_file)

    # Check for epg must be done to prevent that a epg is mapped to physical domains
    if "green_epg" in post_address:
        contract_between_egps = physical_domains['domain_green']
        make_post_request(post_address, connection, contract_between_egps)

    if "red_epg" in post_address:
        contract_between_egps = physical_domains['domain_red']
        make_post_request(post_address, connection, contract_between_egps)
