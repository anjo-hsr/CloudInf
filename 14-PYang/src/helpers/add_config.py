def add_config(netconf_connection):
    config_snippet = """
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<vrf>
			<definition>
				<name>Pinky</name>
				<rd>6.6.6.6:666</rd>
				<address-family>
					<ipv4/>
				</address-family>
				<route-target>
					<export>
						<asn-ip>666:1</asn-ip>
					</export>
					<import>
						<asn-ip>666:1</asn-ip>
					</import>
				</route-target>
			</definition>
		</vrf>
	</native>
    """




    res = netconf_connection.edit_conf(config=config_snippet, target="running")
    print(res)
