connection_parameters = dict({
    ("host", "ios-xe-mgmt.cisco.com"),
    ("port", 10000),
    ("username", "root"),
    ("password", "D_Vay!_10&")
})

datastores = dict([
    ("running", "running"),
    ("startup", "startup"),
    ("candidate", "candidate"),
    ("url", "URL")
])

xml_filters = dict([
    ("vrf", """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <vrf/>
            </native>
        </filter>
    """),
    ("bgp", """
        <filter>
            <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp"/>
        </filter>
    """),
    ("interfaces", """
        <filter>
            <interfaces xmlns="urn:ieft:params:xml:ns:yang:ieft-interfaces">
                <interface/>
            </interfaces>
        </filter>
    """)
])

xml_files = dict([
    ("vrf", "add_vrf.xml"),
    ("bgp_leaf", "add_bgp_leaf.xml"),
    ("bgp_spine", "add_bgp_spine.xml")
])

vrf_parameters = dict([
        ("name", None),
        ("rd_address", None),
        ("rd_port", None),
        ("asn_address", None),
        ("asn_port", None),
    ])