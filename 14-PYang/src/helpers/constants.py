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
    ("filter", None),
    ("changeDevice", None)
])

add_xml_files = dict([
    ("bgp", "add_bgp.xml"),
    ("vlanWithVrf", "add_vlan.xml"),
    ("vrf", "add_vrf.xml")
])

delete_xml_files = dict([
    ("bgp", "delete_bgp.xml"),
    ("vlanWithVrf", "delete_vlan.xml"),
    ("vrf", "delete_vrf.xml")
])

filter_xml_files = dict([
    ("exit", None),
    ("bgp", "filter_bgp.xml"),
    ("vlanWithVrf", "filter_vlan.xml"),
    ("vrf", "filter_vrf.xml")
])

vrf_add_parameters = dict([
    ("name", None),
    ("rd_address", None),
    ("rd_port", None),
    ("asn_address", None),
    ("asn_port", None),
    ("as_id", None)
])

vrf_delete_parameters = dict([
    ("name", None),
    ("as_id", None)
])

bgp_add_parameters = dict([
    ("as_id", None),
    ("remote_id", None),
    ("remote_as", None),
])

bgp_delete_parameters = dict([
    ("as_id", None),
    ("remote_id", None)
])

vlan_add_parameters = dict([
    ("vlan_id", None),
    ("vrf_name", None)
])

vlan_delete_parameters = dict([
    ("vlan_id", None)
])
