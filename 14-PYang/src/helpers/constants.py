# TODO - Undo
# connection_parameters = dict({
#    ("host", "ios-xe-mgmt.cisco.com"),
#    ("port", 10000),
#    ("username", "root"),
#    ("password", "D_Vay!_10&")
# })

connection_parameters = dict({
    ("host", "SW03-pod-9.lab.ins.hsr.ch"),
    ("port", 830),
    ("username", "ins"),
    ("password", "ins@lab")
})

clean_connection_parameters = dict({
    ("host", None),
    ("port", None),
    ("username", None),
    ("password", None)
})

methods = dict([
    ("exit", None),
    ("add", None),
    ("delete", None),
    ("displayAll", None),
    ("filter", None)
])

add_xml_files = dict([
    ("bgp", "add_bgp.xml"),
    ("vlan", "add_vlan.xml"),
    ("vrf", "add_vrf.xml")
])

delete_xml_files = dict([
    ("bgp", "delete_bgp.xml"),
    ("vrf", "delete_vrf.xml")
])

vrf_add_parameters = dict([
    ("name", None),
    ("rd_address", None),
    ("rd_port", None),
    ("asn_address", None),
    ("asn_port", None),
    ("as_id", None)
])

bgp_add_parameters = dict([
    ("as_id", None),
    ("remote_id", None),
    ("remote_as", None),
])

vrf_delete_parameters = dict([
    ("name", None),
    ("as_id", None),
    ("vlan_id", None)
])

vlan_add_parameters = dict([
    ("vlan_id", None),
    ("vrf_name", None)
])
