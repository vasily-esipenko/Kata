# 7 kyu kata
# List Filtering
# Link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# Description:

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# My solution:


def filter_list(l):
    new_l = []
    for i in l:
        if type(i) is int:
            new_l.append(i)
    return new_l


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
