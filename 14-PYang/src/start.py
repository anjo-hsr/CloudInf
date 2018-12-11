from src.helpers.get_config import get_config
from src.helpers.print_config import print_config
from src.helpers.connection_handler import generate_connection

connection_settings = dict([
    #("HOST", "SW03-pod-1.lab.ins.hsr.ch"),
    #("PORT", 830),
    #("USER", "ins"),
    #("PASSWORD", "ins@lab"),
    ("HOST", "ios-xe-mgmt.cisco.com"),
    ("PORT", 10000),
    ("USER", "root"),
    ("PASSWORD", "D_Vay!_10&")
])

sources = dict([
    ("running", "running"),
    ("startup", "startup"),
    ("candidate", "candidate"),
    ("url", "URL")
])

xml_map = dict([
    ("vrf", """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <vrf/>
            </native>
        </filter>
    """),
    ("bpg", """
        <filter>
            <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
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

netconf_connection = generate_connection(connection_settings)
# add_config(netconf_connection)
# Show running-config
# config = netconf_connection.get_config("running")

# Show Services


xml_string = xml_map["vrf"]
config = get_config(sources["running"], netconf_connection, xml_string)

print_config(config)

netconf_connection.close_session()
