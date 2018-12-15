from colorama import Back, Fore, Style


def get_info_string(string_value):
    return Back.LIGHTGREEN_EX + string_value + Back.RESET


def get_successful_string(string_value):
    return Back.LIGHTGREEN_EX + string_value + Back.RESET


def get_error_string(string_value):
    return Back.LIGHTGREEN_EX + string_value + Back.RESET


def get_bold_string(string_value):
    return Style.BRIGHT + string_value + Style.RESET_ALL


colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]


def get_next_fore_color(color_counter):
    return colors[color_counter % len(colors) - 1]
