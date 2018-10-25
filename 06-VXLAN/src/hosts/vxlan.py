import sys

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

from helpers.helper_system import get_peers, terminate_sessions
from helpers.helper_network import add_hosts_to_network, add_switch_to_network, add_controller_to_network
from helpers.helper_vxlan import map_vxlans
from helpers.helper_switch import map_hosts_with_switch, configure_switch
from helpers.helper_print import print_node_ips


def new_network(max_vlans, max_hosts_per_vlan):
    peers = get_peers()
    network = Mininet()

    add_hosts_to_network(network, max_vlans, max_hosts_per_vlan)
    switch = add_switch_to_network(network)
    add_controller_to_network(network)

    map_hosts_with_switch(network, switch)

    network.start()

    configure_switch(network)

    print_node_ips(network)

    map_vxlans(network, peers, max_vlans)
    CLI(network)

    network.stop()


if __name__ == "__main__":
    terminate_sessions()

    setLogLevel("info")
    new_network(int(sys.argv[1]), int(sys.argv[2]))
