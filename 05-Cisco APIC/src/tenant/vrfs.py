from src.helpers.helper_json_files import json_file_to_post_requests, make_post_request
import json


def generate_vrfs(connection):
    file_path = "./_json_files/tenant/vrfs.json"
    json_file_to_post_requests(connection, file_path, "vrf_array", "fvCtx")


def bind_vrfs(connection, bd_name, vrf_name):
    mapping = {}
    mapping["fvRsCtx"] = {}
    mapping["fvRsCtx"]["attributes"] = {}
    mapping["fvRsCtx"]["attributes"]["tnFvCtxName"] = vrf_name
    mapping["fvRsCtx"]["children"] = []

    print(mapping)

    post_address = "https://10.18.1.10/api/node/mo/uni/tn-group1/BD-" + bd_name + "/rsctx.json"
    make_post_request(post_address, connection, mapping)
