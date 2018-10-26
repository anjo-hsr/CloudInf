from helper_host import generate_hosts, get_hex_host_id
from mininet.node import RemoteController


def add_hosts_to_network(network, max_vlans, max_hosts_per_vlan):
    counter = 1
    while counter <= max_hosts_per_vlan:
        generate_hosts(counter, max_vlans, network)
        counter += 1


def add_switch_to_network(network):
    return network.addSwitch("s" + get_hex_host_id())


def add_controller_to_network(network):
    network.addController(name='ryuController',
                          controller=RemoteController,
                          ip='192.168.72.100',
                          port=6633)
