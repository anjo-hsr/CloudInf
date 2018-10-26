from hashlib import sha256

from helper_vlan import generate_vlan_array
from helper_switch import get_switch_ip_address


def generate_vxlan_tunnels(ip_address, max_vlans, switch):
    ips = [ip_address, get_switch_ip_address(switch)]
    for vlan in generate_vlan_array(max_vlans):
        print(str(min(ips)) + "-" + str(max(ips)) + " - vlan" + str(vlan))
        vxlan_tag = __connection_string_to_hash(ips, vlan)

        switch.cmdPrint(
            "ovs-vsctl add-port " + str(switch) + " vx" + str(vxlan_tag) + " tag=" + str(vlan) +
            " -- set interface vx" + str(vxlan_tag) + " type=vxlan option:remote_ip=" + ip_address +
            " option:key=" + str(vxlan_tag))


def __connection_string_to_hash(ips, vlan):
    ip_string = str(min(ips)) + "-" + str(max(ips)) + "-" + str(vlan)
    hash_value = sha256(ip_string.encode("utf-8"))
    return int(hash_value.hexdigest()[:4], 16) + 4096


def map_vxlans(network, peers, max_vlans):
    for ip_address in peers:
        for switch in network.switches:
            if ip_address != get_switch_ip_address(switch):
                generate_vxlan_tunnels(ip_address, max_vlans, switch)
