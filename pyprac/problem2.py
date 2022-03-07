"""
Problem 2: If else, For Loop, While
--------------
1. If, elif, else ( Fizz Buzz FizzBuzz for given number )
2. for ( check if number is prime number )
3. while ( print all prime number until given number )
4. break ( for...else ), continue, pass
5. match case
6. Exception handling
7. functions
    indentation
    default parameters
    multiple parameters
    positional parameters - on manoj
    doc string func.__doc__
--------------
"""

from colorama import Fore, Style


def print_color(message, color):
    print(Style.BRIGHT)
    print(color, message)
    print(Style.RESET_ALL)


def print_success(message):
    print_color(message, Fore.GREEN)


def print_failure(message):
    print_color(message, Fore.RED)

def fizz_buzz(num=15):
    '''
    Determine if the given number is Fizz / Buzz / FizzBuzz
    :param num: Number to Evaluate
    :return: A FizzBuzz string
    '''

    output = ""
    if num % 15 == 0:
        output = "FizzBuzz"
    elif num % 5 == 0:
        output = "Buzz"
        if num % 2 == 0:
            output = f"Even {output}"
        else:
            output = f"Odd {output}"
    elif num % 3 == 0:
        output = "Fizz"
        if num % 2 == 0:
            output = f"Even {output}"
        else:
            output = f"Odd {output}"
    else:
        output = "None"

    return output

"""
if __name__ == "__main__":
    '''
    print("Print running standalone")
    # FizzBuzz print out numbers 3 = Fizz, 5 = Buzz & 3 & 5 = FizzBuzz
    number = int(input("Enter a Number: "))
    result = fizz_buzz(number)
    print(result)
    
    number = int(input("Enter a Number: "))
    for cur_number in range(1, number + 1):
        cur_result = fizz_buzz(cur_number)
        print_str = f'{cur_number}: {cur_result}'
        if cur_result == 'None':
            print_failure(print_str)
        else:
            print_success(print_str)
    '''
else:
    print("Called from a diff module")


class Vehicle:
    '''
    This is a simple Vehicle Class
    '''

    PI = 3.14

    def __str__(self):
        return f"PI value is {self.PI}"
"""

# number = int(input("Enter a Number: "))
'''
even_number = []
odd_number = []

for cur_number in range(1, number + 1):
    if cur_number % 2 == 0:
        even_number.append(cur_number)
    else:
        odd_number.append(cur_number)

print_success('Even Number'.center(20, "-"))
for cur_number in even_number:
    print(cur_number)
print_success(''.center(20, "-"))

print_success('Odd Number'.center(20, "*"))
for cur_number in odd_number:
    print(cur_number)
print_success(''.center(20, "*"))

while True:
    print(number)
    number -= 1
    if number > 0:
        continue
    else:
        break


while number > 0:
    print(number)
    number -= 1


def some_function():
    pass



for cur_number in range(1, number + 1):
    if cur_number % 2 == 0:
        if cur_number == 4:
            print("I don't wish to print this")
            break
        else:
            print(cur_number)
    else:
        print(cur_number)
else:
    print("Else part")
    
number = int(input("Enter a Number: "))
match number:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case _:
        print('I don\'t know')
'''


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

'''
num1 = get_number(1, 10)
num2 = get_number(0, 10)

try:
    result = num1 / num2
    print_success(result)
except ZeroDivisionError as e:
    print(f'Second Number cannot be zero')
    print(e)
except Exception as e_all:
    print(f"Something else: {e_all}")
finally:
    print("Done")
'''
