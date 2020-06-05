# 6kyu kata
# Find the odd int
# Link: https://www.codewars.com/kata/54da5a58ea159efa38000836
# Description:
# Given an array, find the integer that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.


# My solution:


def find_it(seq):
    for i in seq:
        seq.count(i)
        if seq.count(i) % 2 != 0:
            return i


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
