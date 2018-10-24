from curses.ascii import isprint

from helper_host import get_host_id
from helper_vlan import get_vlan_id


def get_switch_ip_address(switch):
    ip_string = switch.cmd(
        "ifconfig eth0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*'")
    return ''.join(char for char in ip_string if isprint(char))


def map_hosts_with_switch(network, switch):
    for host in network.hosts:
        network.addLink(switch, host)
        print(str(switch) + " - " + str(host))


def add_vlan_to_switchports(network, switch):
    port_counter = 1
    for host in network.hosts:
        vlan_id = get_vlan_id(host, get_host_id())
        switch.cmdPrint("ovs-vsctl set port s" + get_host_id() + "-eth" + str(port_counter) + " tag=" + str(vlan_id))

        port_counter += 1

def configure_switch(network):
    for switch in network.switches:
        switch.cmdPrint("ovs-vsctl set-fail-mode s" + get_host_id() + " standalone")
        switch.cmdPrint("ovs-ofctl -O OpenFlow13 s" + get_host_id())
        add_vlan_to_switchports(network, switch)
