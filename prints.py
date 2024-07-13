from colorama import Fore, Style


def print_success(message):
    print(Fore.GREEN + Style.BRIGHT + message + Fore.RESET)


def print_fail(message):
    print(Fore.RED + Style.BRIGHT + message + Fore.RESET)


def print_info(message):
    print(Fore.BLUE + Style.BRIGHT + message + Style.RESET_ALL + Fore.RESET)
