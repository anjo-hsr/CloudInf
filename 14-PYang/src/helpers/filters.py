xml_filters = dict([
    ("exit", None),
    ("vlan", """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <Vlan/>
                </interface>
            </native>
        </filter>
    """),
    ("vrf", """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <vrf/>
            </native>
        </filter>
    """),
    ("get_vrf", """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <vrf>
                <name>{{vrf_name}}</name>
                </vrf>
            </native>
        </filter>
    """),
    ("bgp", """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router>
                    <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp"/>
                </router>
            </native>
        </filter>
    """),
])