import sys, os
import socket, subprocess
from curses.ascii import isprint

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info


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


def get_vlan_id(host, host_id):
    client_id = int(str(host).replace("h" + host_id, ""))
    return (client_id - (client_id % 100)) / 10


def get_host_id():
    return socket.gethostname().replace("vxlan-", "")


def add_hosts_to_network(network, max_vlans, max_hosts_per_vlan):
    counter = 1
    while counter <= max_hosts_per_vlan:
        generate_vlan_host(counter, max_vlans, network)
        counter += 1


def generate_vlan_array(max_vlans):
    vlan_steps = 10
    return range(10, max_vlans * vlan_steps + 1, vlan_steps)


def generate_vlan_host(counter, max_vlans, network):
    for vlan in generate_vlan_array(max_vlans):
        host = generate_host(vlan, counter)
        network.addHost(name=host["hostname"], ip=host["ip_address"], mac=host["mac_address"])


def generate_host(vlan_id, counter):
    host_id = get_host_id()
    basic_host_name = "h" + host_id
    hostname = basic_host_name + str(vlan_id / 10) + str(counter).zfill(2)
    ip_address = "10." + str(vlan_id / 10) + "." + host_id + str(vlan_id / 10) + "." + str(counter) + "/16"
    mac_address = "00:00:00:0" + host_id + ":0" + str(vlan_id / 10) + ":0" + str(counter)
    return {"hostname": hostname, "ip_address": ip_address, "mac_address": mac_address}


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


def print_node_ips(network):
    for switch in network.switches:
        print(str(switch) + ": " + switch.cmd("ifconfig | grep 'inet addr:' | grep -v 127"))
    for host in network.hosts:
        print(str(host) + ": " + host.cmd("ifconfig | grep '10\.'"))


def get_switch_ip_address(switch):
    ip_string = switch.cmd(
        "ifconfig eth0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*'")
    return ''.join(char for char in ip_string if isprint(char))


def generate_vxlan_tunnels(ip_address, max_vlans, switch):
    ips = [ip_address, get_switch_ip_address(switch)]
    for vlan in generate_vlan_array(max_vlans):
        print(str(min(ips)) + "-" + str(max(ips)) + " - vlan" + str(vlan))
        vxlan_tag = hash(str(min(ips)) + "-" + str(max(ips)) +
                         "-" + str(vlan)) & 10000000

        switch.cmdPrint(
            "ovs-vsctl add-port " + str(switch) + " vx" + str(vxlan_tag) + " tag=" + str(vlan) +
            " -- set interface vx" + str(vxlan_tag) + " type=vxlan option:remote_ip=" + ip_address +
            " option:key=" + str(vxlan_tag))


def map_vxlans(network, peers, max_vlans):
    for ip_address in peers:
        for switch in network.switches:
            if ip_address != get_switch_ip_address(switch):
                generate_vxlan_tunnels(ip_address, max_vlans, switch)


def new_network(peers, max_vlans, max_hosts_per_vlan):
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


def terminate_sessions():
    # Terminate current sessions with mn -c
    subprocess.check_output(['bash', '-c', "mn -c &> /etc/null"])


if __name__ == "__main__":
    terminate_sessions()

    setLogLevel("info")
    peers = get_peers()
    new_network(peers, int(sys.argv[1]), int(sys.argv[2]))
