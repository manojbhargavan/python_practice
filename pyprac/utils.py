from colorama import Fore, Style


def print_color(message, color):
    print(Style.BRIGHT)
    print(color, message)
    print(Style.RESET_ALL)


def print_success(message):
    print_color(message, Fore.GREEN)


def print_failure(message):
    print_color(message, Fore.RED)


def get_number(min_num=1, max_num=10, message=""):
    got_the_number = False
    output = -1

    while not got_the_number:
        if message == "":
            message = "Give me a number please: "

        user_num = input(message)

        if user_num.isdigit():
            output = int(user_num)
            if output >= min_num and output <= max_num:
                print_success(f"Thank you!!")
                got_the_number = True
            else:
                print_failure(f"Number should be between {min_num} and {max_num}")
        else:
            print_failure(f"Give me a digit please")

    return output


def reverse_str(input_str):
    """
    Reverse a string
    """
    return input_str[::-1]
