from src.helpers.connection_handler import check_connection, generate_connection
from src.helpers.input_handler import get_add_configs, get_connection, get_datastore, get_filter
from src.helpers.constants import datastores
from src.helpers.get_config import get_config, get_filtered_config
from src.helpers.print_config import print_config
from src.helpers.xml_parser import add_filter

m = generate_connection(get_connection())
check_connection(m)

datastore = get_datastore()
config = get_config(datastore, m)

filter = get_filter()
xml_filter = add_filter(config, filter)
config = get_filtered_config(datastores["running"], m, xml_filter)

add_xml_config = get_add_configs()

print_config(config)

m.close_session()
exit()
