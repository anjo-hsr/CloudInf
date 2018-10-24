from helper_host import generate_hosts


def add_hosts_to_network(network, max_vlans, max_hosts_per_vlan):
    counter = 1
    while counter <= max_hosts_per_vlan:
        generate_hosts(counter, max_vlans, network)
        counter += 1
