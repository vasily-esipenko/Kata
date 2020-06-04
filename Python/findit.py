# 6kyu kata
# Find the odd int
# Link: https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    for i in seq:
        seq.count(i)
        if seq.count(i) % 2 != 0:
            return i
