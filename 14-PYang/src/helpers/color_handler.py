from colorama import Back, Fore


def get_background_colored_string(string_value):
    return Back.LIGHTGREEN_EX + string_value + Back.RESET


colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW]


def get_next_fore_color(color_counter):
    return colors[color_counter % len(colors) - 1]
