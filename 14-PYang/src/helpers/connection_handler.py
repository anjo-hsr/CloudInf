from ncclient import manager


def generate_connection(connection_parameters):
    host = connection_parameters["host"]
    port = connection_parameters["port"]
    username = connection_parameters["username"]
    password = connection_parameters["password"]
    return manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
                           look_for_keys=False, allow_agent=False)


def check_connection(m):
    if not m.connected:
        print("Connection was closed. You were not longer connected to the server")
        exit(1)