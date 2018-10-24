import sys

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

from helpers.helper_host import get_host_id
from helpers.helper_system import get_peers, terminate_sessions
from helpers.helper_vxlan import map_vxlans
from helpers.helper_switch import map_hosts_with_switch, add_vlan_to_switchports
from helpers.helper_print import print_node_ips
from helpers.helper_network import add_hosts_to_network


def new_network(max_vlans, max_hosts_per_vlan):
    peers = get_peers()
    network = Mininet()

    add_hosts_to_network(network, max_vlans, max_hosts_per_vlan)

    switch = network.addSwitch("s" + get_host_id())

    map_hosts_with_switch(network, switch)

    network.start()

    for switch in network.switches:
        switch.cmdPrint("ovs-vsctl set-fail-mode s" + get_host_id() + " standalone")
        add_vlan_to_switchports(network, switch)

    print_node_ips(network)

    map_vxlans(network, peers, max_vlans)
    CLI(network)

    network.stop()


if __name__ == "__main__":
    terminate_sessions()

    setLogLevel("info")
    new_network(int(sys.argv[1]), int(sys.argv[2]))
