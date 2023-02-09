##########################################################################
# The Fence
#
# We have a fence that is made of n wooden boards that are nailed
# together. In addition, we are given a list of characters that represent
# different colors; for example ['W', 'R', 'B']. (Suppose that 'W' stands
# for white, 'B' for blue and 'R' for red.) 
#
# Our task is to color the fence.
##########################################################################

##########################################################################
# Write a function all_colorings(n, c) that takes an integer n which is
# the length of the fence (i.e. the number of wooden boards) and a list
# of characters c (i.e. the list of possible colors). The functions should
# return a list of strings where each string represents one possible
# coloring of the fence. The elements of the list may be in ANY order.
#
# Examples:
#
#     >>> all_colorings(4, ['W', 'R', 'B'])
#     ['WWWW', 'WWWR', 'WWWB', 'WWRW', 'WWRR', 'WWRB', 'WWBW', 'WWBR', 
#      'WWBB', 'WRWW', 'WRWR', 'WRWB', 'WRRW', 'WRRR', 'WRRB', 'WRBW', 
#                 <<< 49 elements were omitted >>>
#      'BRWB', 'BRRW', 'BRRR', 'BRRB', 'BRBW', 'BRBR', 'BRBB', 'BBWW', 
#      'BBWR', 'BBWB', 'BBRW', 'BBRR', 'BBRB', 'BBBW', 'BBBR', 'BBBB']
#     >>> len(all_colorings(4, ['W', 'R', 'B']))
#     81
#     >>> all_colorings(3, ['W', 'R'])
#     ['WWW', 'WWR', 'WRW', 'WRR', 'RWW', 'RWR', 'RRW', 'RRR']
#
# Hint: Can you use recursion?
##########################################################################

def all_colorings(n, c):
    if n == 1:
        return c

    new_colorings = []
    for fence in all_colorings(n-1, c):
        for colour in c:
            new_colorings.append(colour + fence)
    new_colorings.sort()

    return new_colorings


##########################################################################
# Write a function proper_colorings(n, c) which is similar to the previous
# one, except that no two consecutive boards are allowed to have the same
# color. For example, 'WRBW' is a proper coloring; 'BRRW' is NOT allowed
# (the 2nd and the 3rd board are both of color 'R'). The elements of the
# list may be in ANY order.
#
# Examples:
#
#     >>> proper_colorings(4, ['W', 'R', 'B'])
#     ['WRWR', 'WRWB', 'WRBW', 'WRBR', 'WBWR', 'WBWB', 'WBRW', 'WBRB', 
#      'RWRW', 'RWRB', 'RWBW', 'RWBR', 'RBWR', 'RBWB', 'RBRW', 'RBRB', 
#      'BWRW', 'BWRB', 'BWBW', 'BWBR', 'BRWR', 'BRWB', 'BRBW', 'BRBR']
#     >>> len(proper_colorings(4, ['W', 'R', 'B']))
#     24
#     >>> proper_colorings(3, ['W', 'R'])
#     ['WRW', 'RWR']
##########################################################################

def proper_colorings(n, c):
    all_colorings_l = all_colorings(n, c)
    res_l = []
    for i in all_colorings_l:
        counter = 0
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                counter += 1
                break
        if counter == 0:
            res_l.append(i)

    return res_l


##########################################################################
# It turns out that we often do not have unlimited amount of paint.
# Suppose that we have enough paint to color 2 boards with color 'W',
# 3 boards with color 'R' and 1 board with color 'B'. We can give this
# information as a list of pairs:
#
#     [('W', 2), ('R', 3), ('B', 1)]
#
# Write a function proper_limited(n, c) that takes two arguments: n is
# the length of the fence and c is a list of pairs (as described above).
# The function should return a list of all proper colorings where you
# also have to take into account that you only have a limited amound of
# paint. The elements of the list may be in ANY order.
#
# Example:
#
#     >>> proper_limited(5, [('W', 2), ('R', 3), ('B', 1)])
#     ['RWBRW', 'WRBRW', 'RBWRW', 'BRWRW', 'RWRBW', 'WRBWR', 'RWBWR',
#      'WBRWR', 'RBRWR', 'BWRWR', 'RWRWR', 'WRWBR', 'RWRBR', 'RWRWB',
#      'WRWRB']
##########################################################################
def proper_limited(n, c):
    dict_c = {}
    for i in c:
        dict_c[i[0]] = i[1]

    s = ''
    for i in list(dict_c.keys()):
        s += i

    res_l = []
    all_colorings_l = proper_colorings(n, s)
    for comb in all_colorings_l:
        dict_colour = {}
        for colour in comb:
            if colour not in list(dict_colour.keys()):
                dict_colour[colour] = 0
            dict_colour[colour] += 1

        counter = 0
        for j in list(dict_colour.keys()):
            counter = 0
            if dict_colour[j] > dict_c[j]:
                counter += 1
                break

        if counter == 0:
            res_l.append(comb)

    return res_l
