# 6 kyu kata
# Find within array
# Link: https://www.codewars.com/kata/51f082ba7297b8f07f000001

# Description:

# We'll create a function that takes in two parameters:
# a sequence (length and types of items are irrelevant)
# a function (value, index) that will be called on members of the sequence and their index. 
# The function will return either true or false.
# Your function will iterate through the members of the sequence in order until the provided function returns true; at which point your function will return that item's index.
# If the function given returns false for all members of the sequence, your function should return -1.

# My solution:


def find_in_array(seq, predicate): 
    for i in range(0, len(seq)):
        if predicate(seq[i], i):
            return i
    else:
        return -1


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
