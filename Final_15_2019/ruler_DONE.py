##########################################################################
# Ruler
#
# A ruler is a straight strip of plastic, wood, metal, or other material,
# marked at regular intervals and used to draw straight lines or measure
# distances.
#
# A ruler of length 7 can be drawn like this:
#
#     |-|-|-|-|-|-|-|
#     0 1 2 3 4 5 6 7
#
# We will be dealing with rulers which are missing some of the markings.
# For example, the following ruler:
#
#     |---|-|---|---|
#     0   2 3   5   7
#
# has length 7, but only 5 markings. Such a ruler can be represented by
# a list [0, 2, 3, 5, 7]. The list will have the following properties:
#
#  * elements are ordered increasingly;
#  * 0 is always the first element;
#  * the last element is the length of the ruler.
#
# Even if some of the marking are missing, it is still possible that
# the distance can be measured in another way. For example, the marking
# 1 is missing, but the distance 1 can be measured because there are
# markings 2 and 3 (at distance 1). Also, marking 4 is missing but the
# distance 4 can be measured because there are markings 3 and 7 (at
# distance 4).
##########################################################################

##########################################################################
# Write a function distances(ruler) that will take a list of numbers
# that represent a ruler. The function should return a list of all
# distances that can be measured using that ruler. The numbers in that
# list should be sorted (see examples below). If a distance can be
# measured in more than one way, then the number should appear more than
# once in the list.
#
# Examples:
#
#     >>> distances([0, 1, 4, 6])
#     [1, 2, 3, 4, 5, 6]
#     >>> distances([0, 2, 3, 5, 7])
#     [1, 2, 2, 2, 3, 3, 4, 5, 5, 7]
#     >>> distances([0, 1, 2, 3])
#     [1, 1, 1, 2, 2, 3]
##########################################################################

def distances(ruler):
    res_distance = []
    for i in range(len(ruler)):
        for j in range(i+1, len(ruler)):
            res_distance.append(ruler[j] - ruler[i])

    res_distance.sort()
    return res_distance


##########################################################################
# A ruler of length m is called perfect if all the distances 1, 2, ..., m
# can be measured.
#
# For example, the ruler [0, 2, 3, 5, 7] is NOT perfect because the
# distance 6 can not be measured. Write a function is_perfect(ruler) 
# that will take a list of numbers that represent a ruler. The function
# should return True if the ruler is perfect and False otherwise.
#
# Examples:
#
#     >>> is_perfect([0, 1, 4, 6])
#     True
#     >>> is_perfect([0, 2, 3, 5, 7])
#     False
#     >>> is_perfect([0, 1, 2, 3])
#     True
##########################################################################

def is_perfect(ruler):
    all_l = list(set(distances(ruler)))
    for i in range(1, max(ruler) + 1):
        if i not in all_l:
            return False
    return True


##########################################################################
# Write a function all_rulers(length, markings) that takes two arguments:
# the first argument is the length of the ruler and the second argument is
# the number of markings. The function should return a list of all possible
# rulers with the given properties.
#
# Example:
#
#     >>> all_rulers(6, 4)
#     [[0, 1, 2, 6], [0, 1, 3, 6], [0, 2, 3, 6], [0, 1, 4, 6],
#      [0, 2, 4, 6], [0, 3, 4, 6], [0, 1, 5, 6], [0, 2, 5, 6],
#      [0, 3, 5, 6], [0, 4, 5, 6]]
##########################################################################

def all_rulers(length, markings):
    if length == 1:
        return [0]
    elif markings == 2:
        return [[0, length]]
    else:
        previous_markings = all_rulers(length, markings-1)
        all_markings = []

        for i in previous_markings:
            index = markings-3
            for num in range(i[index] + 1, length):
                i.insert(index+1, num)
                tmp = i.copy()
                all_markings.append(tmp)
                i.remove(num)

        return all_markings


##########################################################################
# Write a function perfect_rulers(length, markings) which is similar to
# the previous one, except that it only returns the perfect rulers.
#
# Example:
#
#     >>> perfect_rulers(6, 4)
#     [[0, 1, 4, 6], [0, 2, 5, 6]]
##########################################################################
def perfect_rulers(length, markings):
    all_markings = all_rulers(length, markings)
    res_l = []
    for comb in all_markings:
        if is_perfect(comb):
            res_l.append(comb)
    return res_l
