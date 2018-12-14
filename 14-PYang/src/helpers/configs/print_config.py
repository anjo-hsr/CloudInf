import xml.dom.minidom as xml
import xmltodict

from src.helpers.input_handler import get_filter
from src.helpers.get_config import get_filtered_config


def print_filtered_config(m, datastore):
    xml_filter_map = get_filter()
    if xml_filter_map.key is not None:
        config = get_filtered_config(m, datastore, xml_filter_map.value)
        __print_config(config, xml_filter_map.key)


def print_all(config):
    __print_config(config, "")


def __print_config(config, key):
    if key == "vrf":
        response_dict = xmltodict.parse(config.xml)
        print("\n----------\nThese are the enabled vrfs:")
        print("\t----------")
        for vrf_definition in response_dict["rpc-reply"]["data"]["native"]["vrf"]["definition"]:
            __print_vrf_definition(vrf_definition)
            print("\t----------")
        print("----------")
        return

    print(xml.parseString(config.xml).toprettyxml())


def __print_vrf_definition(vrf_definition):
    print("\tName: " + vrf_definition.get("name"))
    print("\trd: " + str(vrf_definition.get("rd") or "-"))
    print("\tAddress Family:")

    address_families = vrf_definition.get("address-family")
    if address_families is not None:
        for address_family in vrf_definition.get("address-family"):
            print("\t\t-" + address_family + ": enabled")

    route_target = vrf_definition.get("route-target")
    if route_target is not None:
        print("\tRoute Target:")
        for route_target_type in vrf_definition.get("route-target"):
            print("\t\t-" + route_target_type + ":")
            element = route_target.get(route_target_type)
            if element is not None:
                for key in element.keys():
                    print("\t\t\t-" + key + ": " + element.get(key))
