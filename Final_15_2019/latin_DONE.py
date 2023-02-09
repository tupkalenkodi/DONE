##########################################################################
# Latin squares
#
# A Latin square is an n x n matrix in which each row and each column contains
# all numbers from 1 to n (each exactly once). 
# 
# An example of a latin square:
#
#     l = [[2, 4, 1, 3],
#          [3, 1, 4, 2],
#          [1, 3, 2, 4],
#          [4, 2, 3, 1]]
##########################################################################

##########################################################################
# Write a function is_latin(m) that gets a matrix m and returns True if
# the matrix is a Latin square, and False otherwise.
#
# Examples:
#
#     >>> is_latin([[2, 4, 1, 3], [3, 1, 4, 2], [1, 3, 2, 4], [4, 2, 3, 1]])
#     True
#     >>> is_latin([[2, 4, 1, 3], [3, 1, 4, 2], [1, 3, 2, 4], [4, 2, 1, 3]])
#     False
##########################################################################

def is_latin(m):
    for row in m:
        row_dict = {}
        for num in row:
            if num not in list(row_dict.keys()):
                row_dict[num] = 0
            row_dict[num] += 1

        for number in list(row_dict.keys()):
            if row_dict[number] != 1:
                return False

    for i in range(len(m[0])):
        col_dict = {}
        for row2 in m:
            if row2[i] not in list(col_dict.keys()):
                col_dict[row2[i]] = 0
            col_dict[row2[i]] += 1

        for number2 in list(col_dict.keys()):
            if col_dict[number2] != 1:
                return False

    return True


##########################################################################
# If we swap two columns (or rows) in a Latin square we obtain another
# Latin square. For example, if we swap the first two columns in the Latin
# square l above, we obtain:
#
#         [[4, 2, 1, 3],
#          [1, 3, 4, 2],
#          [3, 1, 2, 4],
#          [2, 4, 3, 1]]
#
# Write a function swapped(m, c, i, j) that gets a matrix m, a character c,
# and indices i and j. The function should return a new Latin square that
# is obtained from m. If c is 'R' then rows i and j should be swapped.
# if c is 'C' then columns i and j should be swapped.
#
# Examples:
#
#     >>> l = [[2, 4, 1, 3], [3, 1, 4, 2], [1, 3, 2, 4], [4, 2, 3, 1]]
#     >>> swapped(l, 'C', 0, 1)
#     [[4, 2, 1, 3], [1, 3, 4, 2], [3, 1, 2, 4], [2, 4, 3, 1]]
#     >>> swapped(l, 'R', 1, 3)
#     [[2, 4, 1, 3], [4, 2, 3, 1], [1, 3, 2, 4], [3, 1, 4, 2]]
##########################################################################

def swapped(m, c, i, j):
    if c == 'R':
        tmp = m[i]
        m[i] = m[j]
        m[j] = tmp

    elif c == 'C':
        for row in m:
            tmp = row[i]
            row[i] = row[j]
            row[j] = tmp

    return m


##########################################################################
# Write a function regular_square(n) that takes an integer n and returns
# a regular n x n Latin square. The first row of a regular Latin square
# is [1, 2, 3, ..., n]. The second row is [2, 3, ..., n, 1] (i.e., it is
# shifted to the left). The third row is [3, 4, ..., n, 1, 2], etc.
#
# Examples:
#
#     >>> regular_square(4)
#     [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
#     >>> regular_square(3)
#     [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
##########################################################################

def regular_square(n):
    if n == 1:
        return [[1]]
    else:
        m = regular_square(n-1)
        new_m = []
        counter = n-1
        tmp2 = []
        for row in m:
            if counter == n-1:
                row.insert(0, n)
                tmp2 = row.copy()
                row.remove(n)

            row.insert(counter, n)
            tmp = row.copy()
            new_m.append(tmp)
            counter -= 1
        new_m.append(tmp2)

        return new_m


##########################################################################
# Write a function make_new(m, op) that takes a Latin square m and a list
# of operations op that contains tuples (c, i, j). The function should
# return a new Latin square that is obtained from m by a sequence of
# swaps. The tuple (c, i, j) means that we should swap rows i and j if
# c is 'R'; if c is 'C' it means that we should swap columns i and j.
#
# Examples:
#
#     >>> make_new(regular_square(4), [('R', 0, 1), ('C', 0, 2), ('R', 0, 3), ('C', 1, 2)])
#     [[2, 4, 1, 3], [3, 1, 2, 4], [1, 3, 4, 2], [4, 2, 3, 1]]
##########################################################################

def make_new(m, op):
    for pair in op:
        m = swapped(m, pair[0], int(pair[1]), int(pair[2]))

    return m
