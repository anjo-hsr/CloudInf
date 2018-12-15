from colorama import Back, Fore, Style


def get_info_string(string_value):
    return Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + string_value + Back.RESET + Fore.RESET


def get_successful_string(string_value):
    return Back.LIGHTGREEN_EX + string_value + Back.RESET


def get_error_string(string_value):
    return Back.LIGHTRED_EX + string_value + Back.RESET


def get_bold_string(string_value):
    return Style.BRIGHT + string_value + Style.RESET_ALL


__colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]


def get_next_fore_color(color_counter):
    return __colors[color_counter % len(__colors) - 1]
