def is_a_parameter_none(vrf_parameters):
    start_boolean = False
    for key in vrf_parameters.keys():
        start_boolean = start_boolean or (vrf_parameters[key] is None)
    return start_boolean


def replace_variables_in_file(filename, parameters):
    with open("./files/" + filename) as xml_file:
        imported_xml_file = xml_file.read()
        for key in parameters.keys():
            imported_xml_file = imported_xml_file.replace("{{" + str(key) + "}}", parameters[key])
    return imported_xml_file
