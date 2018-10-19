from src.helpers.Connection import Connection
from src.helpers.helper_login import login

from src.fabric.vlans import create_vlans
from src.fabric.physical_domains import create_physical_domains
from src.fabric.attachable_access_entity_profiles import attachable_access_entity_profiles
from src.fabric.leaf_switches.leaf_interfaces_policy_groups import create_policy_groups
from src.fabric.leaf_switches.leaf_interfaces_profiles import create_leaf_interfaces_profiles

from src.tenant.contract import generate_default_contracts
from src.tenant.bridge_domains import generate_bridge_domains
from src.tenant.application_profiles import generate_application_profiles
from src.tenant.application_epgs import create_application_epgs

ip_address = raw_input("Please enter Cisco APICs IP address: [10.18.1.10]\t") or "10.18.1.10"
https_address = "https://" + ip_address

login_information = login(https_address)
group_name = login_information[0]
cookie = login_information[1]
token = login_information[2]

connection = Connection(https_address, cookie, token)

# Things in Fabric
create_vlans(connection)
create_physical_domains(connection)
attachable_access_entity_profiles(connection)
create_policy_groups(connection)
create_leaf_interfaces_profiles(connection)

###
# Things in Tenant
# generate_default_contracts(connection)
# generate_bridge_domains(connection)
# generate_application_profiles(connection)
# create_application_epgs(connection)
###
