# 4 kyu kata
# Sum of Intervals
# Link: https://www.codewars.com/kata/52b7ed099cdc285c300001cd

# Description:

# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
# List containing overlapping intervals:
# [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

# My solution:


def sum_of_intervals(intervals):
    result = []
    for i in intervals:
        for j in range(i[0], i[1]):
            result.append(j)
    return len(set(result))


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
