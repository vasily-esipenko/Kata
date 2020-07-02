# 5 kyu kata
# Human Readable Time
# Link: https://www.codewars.com/kata/52685f7382004e774f0001f7

# Description:

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
# You can find some examples in the test fixtures.

# My solution:


def make_readable(seconds):
    res = "{:02d}:{:02d}:{:02d}"
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds %= 60
    return res.format(hours, minutes, seconds)


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
