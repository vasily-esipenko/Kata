# 6 kyu kata
# Create Phone Number
# Link: https://www.codewars.com/kata/525f50e3b73515a6db000b83

# Description:

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

#My solution:


def create_phone_number(n):
    num = "({0}) {1}-{2}"
    first = ""
    second = ""
    third = ""
    for i in range(0, len(n)):
        if i <= 2:
            first += str(n[i])
        elif i <= 5:
            second += str(n[i])
        elif i >= 6:
            third += str(n[i])
    return num.format(first, second, third)


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
