from colorama import Fore, Style
from problem2 import *

print(Fore.RED, 'Hello Python')
print(Style.RESET_ALL, '')

print(Fore.GREEN, fizz_buzz(10))
print(Style.RESET_ALL, '')

if __name__ == "__main__":
    print("main is now main")
else:
    print("Called from a diff module")

car = Vehicle()
print(car)
