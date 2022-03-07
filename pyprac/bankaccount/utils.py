from colorama import Fore, Back, Style


class Utils:

    @staticmethod
    def print_color(message, color):
        print(f'{Style.BRIGHT}{color}{message}{Style.RESET_ALL}')

    @staticmethod
    def print_error(message):
        Utils.print_color(message, Fore.RED)

    @staticmethod
    def print_success(message):
        Utils.print_color(message, Fore.GREEN)

