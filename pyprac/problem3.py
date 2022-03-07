"""
Problem 3: Calculate the number of minutes given days from user
Problem 4: Reverse a String
Problem 5: Palindrome
Problem 6: Get radius of circle from user and print the diameter (2r), circumference (2πr) and area (πr²),
            Ask if he/she want to calculate for new radius, keep asking until user says No or something
--------------
What we learned so far
--------------
"""
from utils import *
from circle import Circle

# Problem 3: Calculate the number of minutes given days from user
user_num = get_number(1, 300, "Give me the number of days and i give the minutes: ")
print_success(f'Minutes in {user_num} days is {user_num * 24 * 60}')

# Problem 4: Reverse a String
user_in = input("Give me a string: ")
output = reverse_str(user_in)
print(output.title())

# Problem 5: Palindrome
user_in = input("Give me a string: ")
output = reverse_str(user_in)
if output == user_in:
    print_success(f'{user_in} is a Palindrome')
else:
    print_failure(f'{user_in} is not a Palindrome')

# Problem 6: Get radius of circle from user and print the diameter (2r), circumference (2πr) and area (πr²),
#             Ask if he/she want to calculate for new radius, keep asking until user says No or something
radius = get_number(1, 300, "Give me the radius of your circle: ")
user_cir = Circle(radius)
print(user_cir)
