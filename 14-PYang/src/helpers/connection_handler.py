from ncclient import manager

from src.helpers.terminal_handler import get_error_string, get_successful_string


def generate_connection(connection_parameters):
    host = connection_parameters["host"]
    port = connection_parameters["port"]
    username = connection_parameters["username"]
    password = connection_parameters["password"]
    return manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
                           look_for_keys=False, allow_agent=False)


def check_connection(m):
    if not m.connected:
        print(get_error_string("Connection was closed. You were not longer connected to the server"))
        exit(1)


def check_and_close_connection(m):
    if m.connected:
        m.close_session()
        if not m.connected:
            print(get_successful_string("\n\nSession closed."))
