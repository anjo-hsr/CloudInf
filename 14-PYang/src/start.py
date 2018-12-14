from src.helpers.connection_handler import check_connection, generate_connection
from src.helpers.input_handler import get_connection, get_datastore, get_filter
from src.helpers.edit_config import add_xml_config, delete_xml_config
from src.helpers.get_config import get_main_config, get_filtered_config
from src.helpers.print_config import print_config, print_and_close

m = generate_connection(get_connection())
check_connection(m)
datastore = get_datastore()

# main_config = get_main_config(datastore, m)

xml_filter = get_filter()
config = get_filtered_config(datastore, m, xml_filter)
print_config(config)

#print_and_close(m, config)

add_xml_config(m, datastore)
delete_xml_config(m, datastore)

m.close_session()
exit()

