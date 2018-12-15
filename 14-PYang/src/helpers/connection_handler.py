from ncclient import manager
import socket

from src.helpers.terminal_handler import get_error_string, get_info_string, get_successful_string


def is_netconf_socket_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if ip is None or port is None:
            return False

        s.connect((ip, int(port)))
        s.shutdown(2)
        print("\n" + get_info_string("Socket is open. Try to connect with given credentials..."))
        return True
    except socket.gaierror:
        print("\n" + get_error_string("No connection to the system possible. Please try again."))
        return False


def generate_connection(connection_parameters):
    host = connection_parameters["host"]
    port = connection_parameters["port"]
    username = connection_parameters["username"]
    password = connection_parameters["password"]
    return manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
                           look_for_keys=False, allow_agent=False)


def check_connection(m):
    if not m.connected:
        print("\n\n" + get_error_string("Connection was closed. You were not longer connected to the server"))
        exit(1)


def check_and_close_connection(m):
    if m.connected:
        m.close_session()
        if not m.connected:
            print("\n\n" + get_successful_string("Session closed."))
