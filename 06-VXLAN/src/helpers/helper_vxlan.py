from helper_vlan import generate_vlan_array
from helper_switch import get_switch_ip_address


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
