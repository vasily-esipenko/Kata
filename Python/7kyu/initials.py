# 7 kyu kata
# C.Wars
# Link: https://www.codewars.com/kata/55968ab32cf633c3f8000008

# Description:

# Normally we have firstname, middle and the last name but there may be more than one word in a name like a South Indian one.
# Similar to those kinda names we need to initialize the names.
# See the pattern below:
# initials('code wars') => returns C.Wars 
# initials('Barack Hussain obama') => returns B.H.Obama 
# Complete the function initials.

# My solution:


def initials(name):
    name = name.split(" ")
    result = ""
    for i in range(0, len(name)-1):
        result += name[i][0].upper() + "."
    return result + name[-1].capitalize()


# My profile on Codewars: https://www.codewars.com/users/vasilyesp
# My StackOverflow account: https://stackoverflow.com/users/13187161/vasily-esipenko
