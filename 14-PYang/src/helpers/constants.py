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

# TODO - Undo
# connection_parameters = dict({
#    ("host", "ios-xe-mgmt.cisco.com"),
#    ("port", 10000),
#    ("username", "root"),
#    ("password", "D_Vay!_10&")
# })

methods = dict([
    ("exit", None),
    ("displayAll", None),
    ("add", None),
    ("filter", None),
    ("delete", None)
])

datastores = dict([
    ("running", "running"),
    ("startup", "startup"),
    ("candidate", "candidate"),
    ("url", "URL")
])

add_xml_files = dict([
    ("exit", None),
    ("vrf", "add_vrf.xml"),
    ("vlan", "add_vlan.xml"),
    ("bgp", "add_bgp.xml")
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
