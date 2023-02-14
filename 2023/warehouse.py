import os

##########################################################################
# There is a warehouse that contains several piles of crates. The drawing
# belows depicts such a warehouse.
#
#               [B]
#               [M]
#   [S]     [T] [Q]        
#   [B]     [C] [F]  
#   [R] [L] [C] [G] 
#   [H] [T] [Z] [S] [P] 
#    0   1   2   3   4   
#
# Each crate is represented by [#] where # is an uppercase letter of the
# English alphabet. (Note that a letter may be used more than once.)
# Stacks are numbered 0 ... n - 1. In the example above n = 5. Assume that
# n <= 10. The above warehouse is also stored in file warehouse.txt.
##########################################################################

# os.mkdir('haha')

##########################################################################
# Write a function load_data(file_name) that gets the name of a file that
# contains the drawing of a warehouse (as described above.) The function
# should return a list of lists that contain crate labels. There should
# be one sublist for each stack of crates. The crate on the bottom should
# be the first element in the list.
#
# Examples:
#
#     >>> load_data('warehouse.txt')
#     [['H', 'R', 'B', 'S'], ['T', 'L'], ['Z', 'C', 'C', 'T'], 
#      ['S', 'G', 'F', 'Q', 'M', 'B'], ['P']]
##########################################################################

def load_data(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    labels = [int(x) for x in lines[-1].split()]
    n = len(labels)
    wh = [[] for i in range(n)]
    # Beware!
    # wh = [[]] * n is BAD! BAD! BAD!
    for h in range(len(lines) - 2, -1, -1):
        for i in range(n):
            if len(lines[h]) > 4*i + 1 and lines[h][4*i + 1] != ' ':
                wh[i].append(lines[h][4*i + 1])
    return wh
    
# print(load_data('warehouse.txt'))

##########################################################################
# Write a function store_data(warehouse, file_name) that gets a list of
# crate stacks and the name of a file. The function should do exactly the
# opposite of load_data. It should print the crates to a text file in the
# format as described above.
#
# Examples:
#
#     >>> wh = [['H', 'R', 'B', 'S'], ['T', 'L'], ['Z', 'C', 'C', 'T'], 
#               ['S', 'G', 'F', 'Q', 'M', 'B'], ['P']]
#     >>> store_data(wh, 'myhouse.txt')
#
# Note that the file myhouse.txt whould be the same as warehouse.txt.
##########################################################################
def store_data(warehouse, file_name):
    h = max([len(column) for column in warehouse])
    c = len(warehouse)
    m = [[' ' for j in range(c * 4)] for i in range(h + 1)]
    for i in range(c):
        m[h][4*i + 1] = str(i)
    for i in range(c):
        for j in range(len(warehouse[i])):
            label = warehouse[i][j]
            m[h - j - 1][4*i + 1] = label
            m[h - j - 1][4*i] = '['
            m[h - j - 1][4*i + 2] = ']'
    f = open(file_name, 'w')
    for line in m:
        print(''.join(line), file=f)
    f.close()
            
wh = [['H', 'R', 'B', 'S'], ['T', 'L'], ['Z', 'C', 'C', 'T'], 
               ['S', 'G', 'F', 'Q', 'M', 'B'], ['P']]
# store_data(wh, 'output/myhouse.txt')

##########################################################################
# We have a crane that is used for moving crates between stacks. The
# crate is controlled by a sequence of commands, where each command
# is a pair (f, t). This means that the crane will move one crate from
# stack f to stack t. For example, the sequence of commands
#
#     (0, 1), (3, 4), (3, 4), (2, 0)
#
# used on the warehouse described in the beginning would result in:     
#               
#   [T]         [Q]        
#   [B] [S] [C] [F] [M] 
#   [R] [L] [C] [G] [B]
#   [H] [T] [Z] [S] [P] 
#    0   1   2   3   4  
#
# Write a function crane(warehouse, command) that gets a list of crate
# stacks and a sequence of command. The function should return a new
# list of crate stacks that are obtained by using the given sequence of
# commands.
#
# Example:
#
#     >>> wh = [['H', 'R', 'B', 'S'], ['T', 'L'], ['Z', 'C', 'C', 'T'], 
#               ['S', 'G', 'F', 'Q', 'M', 'B'], ['P']]
#     >>> crane(wh, (0, 1), (3, 4), (3, 4), (2, 0))
#     [['H', 'R', 'B', 'T'], ['T', 'L', 'S'], ['Z', 'C', 'C'], 
#      ['S', 'G', 'F', 'Q'], ['P', 'B', 'M']]
##########################################################################
def crane(warehouse, command):
    for c in command:
        f, t = c
        crate = warehouse[f].pop()
        warehouse[t].append(crate)
    return warehouse

# print(crane(wh, [(0, 1), (3, 4), (3, 4), (2, 0)]))
##########################################################################
# Your boss is angry, becase he thinks that the crates are badly arranged.
# He insists that all stacks should be of equal height. If this is not
# possible (number of crates is not divisible by the number of stacks),
# then some stacks might be higher by one crate. All such stacks should
# be in the middle of the warehouse. The example above could be rearranged
# like this:        
#               
#       [F] [T] 
#   [B] [B] [C] [F] [Q]
#   [R] [L] [C] [G] [S]
#   [H] [T] [Z] [S] [P] 
#    0   1   2   3   4   
#
# Write a function make_boss_happy(warehouse), that gets a list of crate
# stacks. The function should return a sequence of commands that will make
# the boss happy. If there are several solutions, you may find ANY of them.
# 
# Example:
# 
#     >>> wh = [['H', 'R', 'B', 'S'], ['T', 'L'], ['Z', 'C', 'C', 'T'], 
#               ['S', 'G', 'F', 'Q', 'M', 'B'], ['P']]
#     >>> make_boss_happy(wh)
#     [(3, 1), (0, 4), (3, 1), (3, 4)]
##########################################################################
def make_boss_happy(warehouse):
    total = sum([len(c) for c in warehouse])
    n = len(warehouse)
    goal = [total // n for c in warehouse]
    extra = total % n
    offset = n // 2 - extra // 2
    for i in range(extra):
        goal[i + offset] += 1
    # print(goal)
    commands = []
    while [len(c) for c in warehouse] != goal:
        f, t = None, None
        for i in range(n):
            if len(warehouse[i]) > goal[i]:
                f = i
                break
        for i in range(n):
            if len(warehouse[i]) < goal[i]:
                t = i
                break
        commands.append((f, t))
        warehouse = crane(warehouse, [(f, t)])
    return commands

print(make_boss_happy(wh))
