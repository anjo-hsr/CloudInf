from src.helpers.helper_json_files import json_file_to_data, json_file_to_post_requests, make_post_request


def generate_vrfs(connection):
    file_path = "./_json_files/tenant/vrfs.json"
    json_file_to_post_requests(connection, file_path, "vrf_array", "fvCtx")


def bind_vrfs(connection):
    file_path = "./_json_files/tenant/vrfs_mapping.json"

    data = json_file_to_data(file_path)

    post_address = "https://10.18.1.10/api/node/mo/uni/tn-group1/BD-green-red_BD/rsctx.json"
    make_post_request(post_address, connection, data)
