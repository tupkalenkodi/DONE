##########################################################################
# Numbers
##########################################################################

##########################################################################
# It is known that each natural number n can be expressed as n = 2**k * m,
# where k >= 0 and m is an odd integer. For example, 84 = 2**2 * 21.
# Write a function get_km(n) that gets a number n and returns a tuple
# (k, m), where k and m are defined above.
#
# Examples:
# 
#     >>> get_km(84)
#     (2, 21)
#     >>> get_km(7)
#     (0, 7)
#     >>> get_km(64)
#     (6, 1)
##########################################################################
def get_km(n):
    counter = 0
    while n % 2 == 0:
        counter += 1
        n //= 2
    return counter, n


##########################################################################
# Write a function only_k(l) that gets a list l and returns the number
# k from the expression n = 2**k * m for each number in the list.
#
# Example:
# 
#     >>> only_k([84, 7, 64])
#     [2, 0, 6]
##########################################################################
def only_k(l):
    new_l = []
    for i in l:
        new_l.append(get_km(i)[0])
    return new_l


##########################################################################
# Write a function only_m(l) that gets a list l and returns the number
# m from the expression n = 2**k * m for each number in the list.
#
# Example:
# 
#     >>> only_m([84, 7, 64])
#     [21, 7, 1]
##########################################################################
def only_m(l):
    new_l = []
    for i in l:
        new_l.append(get_km(i)[1])
    return new_l


##########################################################################
# Write a function make_numbers(lk, lm) which takes a list lk and a list
# lm. Lists lk and lm are of equal length. The function should return a
# new list of numbers that are obtained from lists lk and lm.
#
# Example:
# 
#     >>> make_numbers([2, 0, 6], [21, 7, 1])
#     [84, 7, 64]
##########################################################################
def make_numbers(lk, lm):
    res_l = []
    for i in range(len(lk)):
        res_l.append(2 ** lk[i] * lm[i])
    return res_l
