def print_node_ips(network):
    for switch in network.switches:
        print(str(switch) + ": " + switch.cmd("ifconfig | grep 'inet addr:' | grep -v 127"))
    for host in network.hosts:
        print(str(host) + ": " + host.cmd("ifconfig | grep '10\.'"))
