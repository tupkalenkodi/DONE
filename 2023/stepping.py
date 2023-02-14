##########################################################################
# A finite sequence of k numbers is called a stepping sequence if:
#
#    (a) it starts with a 0, and
#    (b) the absolute value of the difference between two consecutive 
#        elements is 1.
#
# Examples of such sequences are:
#    
#    (0, 1, 2, 1, 2, 3, 2, 1)
#    (0, 1, 0, -1, -2, -1, 0, 1)
##########################################################################



##########################################################################
# Write a function is_stepping(l) that gets a tuple (or a list) as its
# only argument. The function should return True if l is a stepping sequence,
# and False if it is not.
#
# Examples:
#
#     >>> is_stepping([0, 1, 2, 1, 2, 3, 2, 1])
#     True
#     >>> is_stepping([0, 1, 2, 2, 3, 2])
#     False
#     >>> is_stepping([-1, -2, -1, 0, 1])
#     False
##########################################################################
def is_stepping(l):
    if l[0] != 0:
        return False
    for i in range(len(l) - 1):
        if abs(l[i] - l[i + 1]) != 1:
            return False
    return True

print(is_stepping([0, 1, 2, 1, 2, 3, 2, 1]))
print(is_stepping([0, 1, 2, 2, 3, 2]))
print(is_stepping([-1, -2, -1, 0, 1]))

##########################################################################
# Write a function make_bound(l) that gets a tuple (or a list) as its
# only argument. Let us denote l = [a_0, a_1, a_2, ..., a_k]. The function
# return a list [x_0, x_1, x_2, ..., x_k] (of the same length as l), 
# where x_i is the smallest number such that -x_i <= a_j <= x_i for all j <= i. 
# (See also examples.)
#
# Examples:
#
#     >>> make_bound([0, 1, 2, 1, 2, 3, 2, 1])
#     [0, 1, 2, 2, 2, 3, 3, 3]
#     >>> make_bound([0, 1, 0, -1, -2, -1, 0, 1])
#     [0, 1, 1, 1, 2, 2, 2, 2]
#     >>> make_bound([-3, 2, -1, -5, 3, -1, 0, 0])
#     [3, 3, 3, 5, 5, 5, 5, 5]
##########################################################################

def make_bound(l):
    x = []
    m = 0
    for c in l:
        if abs(c) > m:
            m = abs(c)
        x.append(m)
    return x

print(make_bound([0, 1, 2, 1, 2, 3, 2, 1]))
print(make_bound([0, 1, 0, -1, -2, -1, 0, 1]))
print(make_bound([-3, 2, -1, -5, 3, -1, 0, 0]))


##########################################################################
# Write a function all_stepping(n) that gets an integer n > 0 as its
# only argument. The function should return a list of all possible stepping
# sequences of length n. (The order of sequences in the list is not important.)
#
# Examples:
#
#     >>> all_stepping(3)
#     [(0, 1, 2), (0, 1, 0), (0, -1, 0), (0, -1, -2)]
#     >>> all_stepping(5)
#     [(0, 1, 2, 3, 4), (0, 1, 2, 3, 2), (0, 1, 2, 1, 2), (0, 1, 2, 1, 0), 
#      (0, 1, 0, 1, 2), (0, 1, 0, 1, 0), (0, 1, 0, -1, 0), (0, 1, 0, -1, -2), 
#      (0, -1, 0, 1, 2), (0, -1, 0, 1, 0), (0, -1, 0, -1, 0), 
#      (0, -1, 0, -1, -2), (0, -1, -2, -1, 0), (0, -1, -2, -1, -2), 
#      (0, -1, -2, -3, -2), (0, -1, -2, -3, -4)]
##########################################################################
def all_stepping(n):
    if n == 1:
        return [(0,)]
    s = all_stepping(n - 1)
    l = []
    for x in s:
        last = x[-1]
        l.append(x + (last - 1,))
        l.append(x + (last + 1,))
    return l

def all_stepping_nonrec(n):
    generation = [(0,)]
    for i in range(n - 1):
        new_gen = []
        for x in generation:
            last = x[-1]
            new_gen.append(x + (last - 1,))
            new_gen.append(x + (last + 1,))
        generation = new_gen
    return generation
        
##########################################################################
# Write a function limited_stepping(n, k) that gets an integer n > 0 and
# an integer k >= 0 as arguments. The function should return a list of all 
# possible stepping sequences of length n, such that all entries are in
# the range -k ... k. (The order of sequences in the list is not important.)
#
# Examples:
#
#     >>> limited_stepping(4, 2)
#     [(0, 1, 2, 1), (0, 1, 0, 1), (0, 1, 0, -1), (0, -1, 0, 1), 
#      (0, -1, 0, -1), (0, -1, -2, -1)]
#     >>> limited_stepping(7, 1)
#     [(0, 1, 0, 1, 0, 1, 0), (0, 1, 0, 1, 0, -1, 0), (0, 1, 0, -1, 0, 1, 0), 
#      (0, 1, 0, -1, 0, -1, 0), (0, -1, 0, 1, 0, 1, 0), (0, -1, 0, 1, 0, -1, 0), 
#      (0, -1, 0, -1, 0, 1, 0), (0, -1, 0, -1, 0, -1, 0)]
##########################################################################
def limited_stepping(n, k):
    l = all_stepping(n)
    m = []
    for x in l:
        if make_bound(x)[-1] <= k:
            m.append(x)
    return m

def limited_stepping_alt(n, k):
    if n == 1:
        return [(0,)]
    s = limited_stepping_alt(n - 1, k)
    l = []
    for x in s:
        last = x[-1]
        if -k <= last - 1 <= k:
            l.append(x + (last - 1,))
        if -k <= last + 1 <= k:
            l.append(x + (last + 1,))
    return l


