from src.helpers.helper_request_generator import make_login_request


def login(https_address):
    group_name = __get_user_name()
    password = __get_password()
    login_response = __get_login_token(https_address, group_name, password)

    token = __extract_token(login_response)
    cookie = __get_session(login_response)

    while token == "":
        print("Login was not correct, please try again.")
        group_name = __get_user_name()
        password = __get_password()
        token = __get_login_token(https_address, group_name, password)

    return [group_name, cookie, token]


def __extract_token(login_response):
    return login_response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]


def __get_session(login_response):
    for cookie in login_response.cookies:
        return cookie.value


def __get_user_name():
    return input("Please enter your login name: [group1]\t") or "group1"


def __get_password():
    return input("Please enter your password: []\t\t\t") or "Lsd8ajYTZk2y"


def __get_login_token(https_address, group_name, password):
    print("Start connection to APIC at " + https_address)

    post_address = https_address + '/api/aaaLogin.json'

    login_response = make_login_request(post_address, {
        "aaaUser": {
            "attributes": {
                "name": group_name,
                "pwd": password
            }
        }
    })

    if login_response.status_code != 200:
        print("Login failed, please check the credentials.")
        return

    return login_response
