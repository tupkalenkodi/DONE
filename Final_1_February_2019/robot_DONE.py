##########################################################################
# The Robot
#
# We have a robot which is located in an infinite plane at coordinates
# (x, y) and is facing direction r, where 0 <= r <= 3. The possible values
# of r have the following meaning:
#
#          (north)
#             0 
#    (west) 3   1 (east)
#             2
#          (south)
#
# You will have to write several functions that will be used to control
# the robot. The current location and direction of the robot can be
# represented by a triple (x, y, r).
##########################################################################

##########################################################################
# Write a function final_destination(p, s) where the argument p is the
# current position of the robot, i.e. a triple (x, y, r); the argument s
# is a string that can contain the following letters:
#
#  * 'R' ... turn to the right (for 90°)
#  * 'L' ... turn to the left (for 90°) 
#  * 'F' ... go forward for 1 unit
#
# The function should return the final position of the robot, i.e. a
# tripe (x', y', r'). 
#
# Examples:
# 
#     >>> final_destination((2, 0, 0), 'FFRFFLFFL')
#     (4, 4, 3)
#     >>> final_destination((2, -1, 0), 'FFFRFFFRFFFRFFFR')
#     (2, -1, 0)
##########################################################################

def final_destination(p, s):
    final = list(p)
    for char in s:
        if char == 'R':
            if final[2] == 3:
                final[2] = 0
            else:
                final[2] += 1
        elif char == 'L':
            if final[2] == 0:
                final[2] = 3
            else:
                final[2] -= 1
        elif char == 'F':
            if final[2] == 0:
                final[1] += 1
            elif final[2] == 1:
                final[0] += 1
            elif final[2] == 2:
                final[1] -= 1
            elif final[2] == 3:
                final[0] -= 1
    return tuple(final)


##########################################################################
# Write a function find_initial(p, s) which takes two arguments: the first
# argument p is the final position of the robot; the argument s is a
# string as defined in the previous function. The function should return
# the starting position of the robot, i.e. it is (in some sense) inverse
# function to final_destination.
# 
# Examples:
#
#     >>> find_initial((4, 4, 3), 'FFRFFLFFL')
#     (2, 0, 0)
#     >>> find_initial((2, -1, 0), 'FFFRFFFRFFFRFFFR')
#     (2, -1, 0)
##########################################################################

def find_initial(p, s):
    initial = list(p)

    new_s = reversed(s)
    for char in new_s:
        if char == 'L':
            if initial[2] == 3:
                initial[2] = 0
            else:
                initial[2] += 1
        elif char == 'R':
            if initial[2] == 0:
                initial[2] = 3
            else:
                initial[2] -= 1
        elif char == 'F':
            if initial[2] == 0:
                initial[1] -= 1
            elif initial[2] == 1:
                initial[0] -= 1
            elif initial[2] == 2:
                initial[1] += 1
            elif initial[2] == 3:
                initial[0] += 1

    return tuple(initial)


##########################################################################
# Write a function final_advanced(p, s) where the argument p is the
# current position of the robot; the argument s is a string that can
# contain letters 'R', 'L' and 'F' as well as numbers. A number k means
# that the command that follows it should be executed k times. For example
# 'L3F4L5F2RFR' is equivalent to 'LFFFLLLLFFFFFRRFR'.
#
#     >>> final_advanced((2, 0, 0), '2FR2FL2FL')
#     (4, 4, 3)
#     >>> final_advanced((2, -1, 0), '3FR3FR3FR3FR')
#     (2, -1, 0)
##########################################################################

def final_advanced(p, s):
    final = list(p)

    multiplier = 0
    counter = 0
    for char in s:
        if char in ['F', 'R', 'L']:
            if counter == 1:
                counter = 0
            else:
                multiplier = 1
        else:
            multiplier = int(char)
            counter += 1
            continue
        for i in range(multiplier):
            if char == 'R':
                if final[2] == 3:
                    final[2] = 0
                else:
                    final[2] += 1
            elif char == 'L':
                if final[2] == 0:
                    final[2] = 3
                else:
                    final[2] -= 1
            elif char == 'F':
                if final[2] == 0:
                    final[1] += 1
                elif final[2] == 1:
                    final[0] += 1
                elif final[2] == 2:
                    final[1] -= 1
                elif final[2] == 3:
                    final[0] -= 1

    return tuple(final)


##########################################################################
# Write a function find_commands(start, end) where the argument start is
# the current position of the robot; the argument end is the final position
# of the robot. The function should return ANY string of commands that
# bring the robot from position start to position end.
#
# Examples:
#
#     >>> find_commands((2, 0, 0), (4, 4, 3))
#     'FFRFFLFFL'
#     >>> find_commands((2, -1, 0), (2, -1, 0))
#     ''
#
# Note: The solution is NOT unique. Your program may return ANY of them.
##########################################################################

def find_commands(start, end):
    s = ''
    robot = list(start)
    if start[1] <= end[1]:
        while robot[2] != 0:
            robot = final_destination(robot, 'R')
            s += 'R'
        while robot[1] != end[1]:
            robot = final_destination(robot, 'F')
            s += 'F'
    elif start[1] > end[1]:
        while robot[2] != 2:
            robot = final_destination(robot, 'R')
            s += 'R'
        while robot[1] != end[1]:
            robot = final_destination(robot, 'F')
            s += 'F'

    if start[0] <= end[0]:
        while robot[2] != 1:
            robot = final_destination(robot, 'R')
            s += 'R'
        while robot[0] != end[0]:
            robot = final_destination(robot, 'F')
            s += 'F'
    elif start[0] > end[0]:
        while robot[2] != 3:
            robot = final_destination(robot, 'R')
            s += 'R'
        while robot[0] != end[0]:
            robot = final_destination(robot, 'F')
            s += 'F'

    while robot[2] != end[2]:
        robot = final_destination(robot, 'R')
        s += 'R'

    return s
