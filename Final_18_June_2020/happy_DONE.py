from itertools import permutations
##########################################################################
# Happy sequences
#
# Let us first implement Euclid's algorithm for finding the greatest common
# divisor of two numbers. The algorithm can be defined recursively:
# 
#     gcd(a, 0) = a
#     gcd(a, b) = gcd(b, a mod b)
#
# where a mod b is the remainder of the integral division of a by b. For
# example:
#
#     gcd(48, 18) = gcd(18, 12) = gcd(12, 6) = gcd(6, 0) = 6.
#
# Define a recursive function gcd(a, b) in Python that will return the
# greatest common divisor of numbers a and b.
#
# Example:
#
#     >>> gcd(48, 18)
#     6
##########################################################################


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


##########################################################################
# A (finite) sequence s_0, s_1, ..., s_{n - 1} of integers is called a
# happy sequence if each two consecutive elements have a common divisor
# which is greater than 1, i.e. if gcd(s_i, s_{i + 1}) > 1 for all i.
#
# In Python, the sequence can be represented by a list [s_0, s_1, ..., s_{n - 1}].
# Write a functions is_happy(l) that will get a list l that contains
# integers. The function should return True if the list contains a happy
# sequence, and False otherwise.
# 
# Examples:
#
#     >>> is_happy([2, 6, 21, 14, 10, 5, 5])
#     True
#     >>> is_happy(is_happy([2, 6, 21, 14, 10, 5, 5]))
#     False
##########################################################################

def is_happy(l):
    for i in range(len(l) - 1):
        if gcd(l[i], l[i+1]) <= 1:
            return False
    return True


##########################################################################
# Write a function happy_sequences(first, rest) that gets two arguments.
# The fist argument is the number s_0 (i.e. the start of the sequences).
# The second argument is a list of integers. The function should return
# the list of all happy sequences that start with the integer first and
# contain all elements from the set rest (in any order). Each possible
# sequence should appear in the list exactly once.
#
# Example:
# 
#     >>> happy_sequences(3, [5, 10, 55, 2, 2, 66])
#     [[3, 66, 55, 5, 10, 2, 2], [3, 66, 2, 2, 10, 5, 55], [3, 66, 2, 2, 10, 55, 5]]
#     >>> happy_sequences(3, [5, 35, 5, 2, 2, 6])
#     []
##########################################################################

def happy_sequences(first, rest):
    all_rest = list(permutations(rest))
    print(len(all_rest))
    res_l = []
    for i in all_rest:
        l_0 = [first] + list(i)
        if is_happy(l_0) and l_0 not in res_l:
            res_l.append(l_0)
    print(len(res_l))
    return res_l


##########################################################################
# Find all happy sequences that contain the following numbers:
#
#     34, 15, 65, 33, 323, 27, 143, 35, 10, 64.
#
# It doesn't matter which number is the starting number.
##########################################################################

def is_happy_all_possibilities(li):
    all_l = list(permutations(li))
    for j in all_l:
        if is_happy(list(j)):
            return j
