connection_parameters = dict({
    ("host", "SW03-pod-9.lab.ins.hsr.ch"),
    ("port", 830),
    ("username", "ins"),
    ("password", "ins@lab")
})

# TODO - Undo
# connection_parameters = dict({
#    ("host", "ios-xe-mgmt.cisco.com"),
#    ("port", 10000),
#    ("username", "root"),
#    ("password", "D_Vay!_10&")
# })

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

add_xml_files = dict([
    ("vrf", "add_vrf.xml"),
    ("bgp_leaf", "add_bgp_leaf.xml"),
    ("bgp_spine", "add_bgp_spine.xml")
])

delete_xml_files = dict([
    ("vrf", "delete_vrf.xml")
])

vrf_add_parameters = dict([
    ("name", None),
    ("rd_address", None),
    ("rd_port", None),
    ("asn_address", None),
    ("asn_port", None),
])

vrf_delete_parameters = dict([
    ("name", None)
])
