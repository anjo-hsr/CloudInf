from helper_system import get_host_id, get_hex_host_id, get_hex_id
from helper_vlan import generate_vlan_array


def generate_hosts(counter, max_vlans, network):
    for vlan in generate_vlan_array(max_vlans):
        host = __generate_host(vlan, counter)
        network.addHost(name=host["hostname"], ip=host["ip_address"], mac=host["mac_address"], vlan=host["vlan"])


def __generate_host(vlan_id, counter):
    host_id = get_host_id()
    basic_host_name = "h" + get_hex_host_id()
    hostname = basic_host_name + str(vlan_id / 10) + str(counter).zfill(2)
    ip_address = "10." + str(vlan_id / 10) + "." + host_id + str(vlan_id / 10) + "." + str(counter) + "/16"
    mac_address = "00:00:00:" + get_hex_host_id() + ":" + get_hex_id(vlan_id / 10) + ":" + get_hex_id(counter)
    return {"hostname": hostname, "ip_address": ip_address, "mac_address": mac_address, "vlan": vlan_id}
