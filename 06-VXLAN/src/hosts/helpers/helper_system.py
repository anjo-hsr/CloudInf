import socket, os
import subprocess


def terminate_sessions():
    # Terminate current sessions with mn -c
    subprocess.check_output(['bash', '-c', "mn -c &> /etc/null"])


def get_peers():
    peer_array = []
    with open('peer_addresses.txt') as peers:
        for peer in peers:
            peer = ''.join(peer.splitlines())
            FNULL = open(os.devnull, "w")
            res = subprocess.call(['ping', '-c', '1', '-l', '1', str(peer)], stdout=FNULL)
            if res == 0:
                peer_array.append(peer)

    return peer_array


def get_host_id():
    return socket.gethostname().replace("vxlan-", "")


def get_hex_host_id():
    return get_hex_id(socket.gethostname().replace("vxlan-", ""))


def get_hex_id(id_number):
    return str("%0.2X" % int(id_number))
