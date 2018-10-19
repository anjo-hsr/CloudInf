from pprint import pprint
import requests


def get_post_address(https_address, dn):
    return https_address + "/api/node/mo/" + dn + ".json"


def make_login_request(post_address, json):
    return requests.post(post_address, verify=False, json=json)


def make_post_request(post_address, connection, json):
    response = requests.post(post_address, verify=False, json=json,
                             headers={"APIC-challenge": connection.get_token(),
                                      "Cookie": "APIC-cookie=" + connection.get_cookie()})

    pprint(response.status_code)
    pprint(response.text)

    if response.status_code == 200:
        pprint(json)
        pprint(post_address)

    return response
