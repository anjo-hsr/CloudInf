from src.helpers.helper_request_generator import make_post_request
from src.helpers.helper_json_files import generate_json_from_file


def __bind_contracts_between(connection, post_address):
    with open('./_json_files/tenant/contracts/application_epg_contracts_between.json') as contracts_between_egps_file:
        contracts_between_egps = generate_json_from_file(contracts_between_egps_file)

    for contract_between_egps in contracts_between_egps['application_epg_contracts_between_epgs_array']:
        make_post_request(post_address, connection, contract_between_egps)


def __bind_contracts_to_blue(connection, post_address):
    with open('./_json_files/tenant/contracts/application_epg_contract_to_blue.json') as contracts_to_blue_file:
        contracts_to_blue = generate_json_from_file(contracts_to_blue_file)

    for contract_to_blue in contracts_to_blue['application_epg_contracts_to_blue_array']:
        make_post_request(post_address, connection, contract_to_blue)


def bind_contracts(connection, post_address):
    __bind_contracts_between(connection, post_address)
    __bind_contracts_to_blue(connection, post_address)
