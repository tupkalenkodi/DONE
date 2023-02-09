##########################################################################
# Coins
# 
# There are five boxes with integral labels from 1 to 5. Let b[i], 0 <= i <= 4,
# denote the i-th box. Initially, each box contains one coin, i.e.
# 
#     b[0] = ... = b[4] = 1.
#
# You may make moves of two different types (in any order):
#
# (a) Remove a coin from a (non-empty) box b[i] and place two coins in
#     b[i + 1]. Of course, this can only be done for 0 <= i <= 3.
#
# (b) Remove a coin from a (non-empty) box b[i] and switch the contents
#     of b[i + 1] and b[i + 2]. Of course, this can only be done for
#     0 <= i <= 2.
#
# The main problem is: What is the largest number of coins that you can
# obtain in b[5]? We are not going to solve this problem, but we will
# produce some code that will help us think about this.
##########################################################################

##########################################################################
# Write a function move_a(state, i) that will get two arguments. The
# first argument state is a tuple of 5 non-negative integers, i.e. the
# number of coins in the five boxes. The second argument is an integer
# i, 0 <= i <= 3. The function should return a new tuple as described
# above. If the move cannot be done, the function should return None.
# 
# Examples:
#
#     >>> move_a((1, 1, 1, 1, 1), 2)
#     (1, 1, 0, 3, 1)
#     >>> print(move_a((1, 0, 2, 2, 3), 1))
#     None
##########################################################################

def move_a(state, i):
    if 3 >= i >= 0 != state[i]:
        l_coins = list(state)
        l_coins[i] -= 1
        l_coins[i+1] += 2

        return tuple(l_coins)
    return None


##########################################################################
# Write a function move_b(state, i) that will get two arguments. The
# first argument state is a tuple of 5 non-negative integers, i.e. the
# number of coins in the five boxes. The second argument is an integer
# i, 0 <= i <= 2. The function should return a new tuple as described
# above. If the move cannot be done, the function should return None.
# 
# Examples:
#
#     >>> move_b((1, 1, 0, 2, 3), 1)
#     (1, 0, 2, 0, 3)
#     >>> print(move_b((1, 0, 2, 2, 3), 3))
#     None
##########################################################################

def move_b(state, j):
    if 2 >= j >= 0 != state[j]:
        l_coins = list(state)
        l_coins[j] -= 1
        tmp = l_coins[j+1]
        l_coins[j+1] = l_coins[j+2]
        l_coins[j+2] = tmp

        return tuple(l_coins)
    return None


##########################################################################
# Write a function possible_moves(state) that will get a single argument,
# a 5-tuple of non-negative integers that represents the number of coins
# in the five boxes. The function should return a set with all possible
# states that can be obtained from a given state in a single move.
#
# Example:
#
#     >>> possible_moves((1, 1, 1, 1, 1))
#     {(1, 1, 0, 1, 1), (0, 3, 1, 1, 1), (1, 1, 0, 3, 1), (1, 0, 3, 1, 1),
#      (1, 1, 1, 0, 3), (0, 1, 1, 1, 1), (1, 0, 1, 1, 1)}
##########################################################################

def possible_moves(state):
    res_set = set()

    for k in range(0, 4):
        if move_a(state, k) is not None:
            res_set.add(move_a(state, k))
    for j in range(0, 3):
        if move_b(state, j) is not None:
            res_set.add(move_b(state, j))

    return res_set


##########################################################################
# Write a function next_generation(state_set) that will get a single
# argument, i.e. a set of states. The function should return a new set
# that contains all possible states that can be obtained from any state
# from the set state_set in a single move.
#
# Example:
#
#     >>> next_generation({(1, 1, 0, 1, 1), (0, 3, 1, 1, 1), (1, 1, 0, 3, 1),
#         (1, 0, 3, 1, 1), (1, 1, 1, 0, 3), (0, 1, 1, 1, 1), (1, 0, 1, 1, 1)})
#     {(0, 3, 1, 0, 3), (1, 0, 0, 1, 3), (0, 1, 1, 0, 3), (1, 0, 1, 0, 3),
#      (0, 2, 3, 1, 1), (1, 0, 2, 1, 1), (0, 3, 0, 3, 1), (1, 0, 3, 0, 1),
#      (1, 1, 0, 3, 0), (1, 0, 0, 3, 1), (1, 1, 0, 0, 3), (0, 0, 1, 3, 1),
#      (0, 0, 3, 1, 1), (0, 3, 0, 1, 1), (1, 0, 1, 0, 1), (1, 0, 2, 3, 1),
#      (1, 0, 0, 1, 1), (1, 0, 3, 0, 3), (0, 0, 1, 1, 1), (0, 1, 0, 1, 1),
#      (1, 1, 0, 2, 3), (0, 1, 0, 3, 1), (0, 2, 1, 1, 1)}
##########################################################################

def next_generation(state_set):
    res_list = []
    for n in state_set:
        if possible_moves(n) is not None:
            res_list += list(possible_moves(n))

    return set(res_list)


##########################################################################
# Write a function nth_generation(n) that will get a single non-negative
# integer n. The function should start with the set {(1, 1, 1, 1, 1)} and
# then use the function next_generation on it for n times. The function
# should return three arguments: the size of the final set, the maximal
# value of the last component among obtained tuples, and the set of all
# tuples that obtain the maximum value.
#
# Examples:
#
#     >>> nth_generation(0)
#     (1, 1, {(1, 1, 1, 1, 1)})
#     >>> nth_generation(10)
#     (542, 13, {(0, 0, 0, 0, 13), (1, 0, 0, 1, 13)})
#     >>> nth_generation(20)
#     (1891, 23, {(0, 0, 0, 0, 23), (0, 0, 2, 0, 23)})
#     >>> nth_generation(23)
#     (2527, 27, {(0, 0, 1, 0, 27)})
##########################################################################

def nth_generation_helper(n):
    if n == 0:
        return 1, 1, {(1, 1, 1, 1, 1)}
    else:
        set_ret = next_generation(nth_generation_helper(n - 1)[2])
        maximum = 0
        counter = []
        for i in set_ret:
            if i[4] >= maximum:
                maximum = i[4]
                counter.append(i)
        counter2 = set()
        for i in counter:
            if i[4] == maximum:
                counter2.add(i)
        return len(set_ret), maximum, set_ret, counter2


def nth_generation(n):
    partial_res = nth_generation_helper(n)
    if n == 0:
        return 1, 1, {(1, 1, 1, 1, 1)}
    return partial_res[0], partial_res[1], partial_res[3]
