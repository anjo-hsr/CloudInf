def generate_vlan_array(max_vlans):
    vlan_steps = 10
    return range(10, max_vlans * vlan_steps + 1, vlan_steps)


def get_vlan_id(host, host_id):
    client_id = int(str(host).replace("h" + host_id, ""))
    return (client_id - (client_id % 100)) / 10
