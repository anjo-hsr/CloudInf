from ncclient import manager


def generate_connection(connection_dict):
    HOST = connection_dict["HOST"]
    PORT = connection_dict["PORT"]
    USER = connection_dict["USER"]
    PASSWORD = connection_dict["PASSWORD"]
    return manager.connect(host=HOST, port=PORT, username=USER, password=PASSWORD, hostkey_verify=False)
