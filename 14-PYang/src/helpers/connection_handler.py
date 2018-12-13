from ncclient import manager


def generate_connection(connection_dict):
    host = connection_dict["host"]
    port = connection_dict["port"]
    username = connection_dict["username"]
    password = connection_dict["password"]
    return manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
                           look_for_keys=False, allow_agent=False)


def check_connection(m):
    if not m.connected:
        print("Connection was closed. You were not connected to the server")
        exit(1)