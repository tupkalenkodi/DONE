import math
from itertools import permutations
##########################################################################
# Apples
#
# There are apples at various locations in the plane. Locations of
# apples are given by a list of pairs, where each element of the list
# is the location of one such apple (its coordinates in the plane),
# for example:
#
#     [(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)]
#
# A function eq for comparing floats is provided below.
##########################################################################
def eq(a, b, eps=1e-12):
    return abs(a - b) < eps


##########################################################################
# A robot will pick those apples. The initial position of the robot is
# (0, 0). The robot always moves in a straight line in the direction of
# the apple it needs to pick next. 
#
# Write a function robot_distance(l) that gets one argument: a list of
# apples l (each element is a pair of numbers). The function should
# return one number: the total distance travelled by the robot. The
# robot will pick apples in the same order as they apper in the list l.
#
# Example: 
#
#     >>> robot_distance([(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)])
#     53.40159303809622
##########################################################################
def robot_distance(l):
    distance = 0
    robot = (0, 0)
    for i in l:
        distance += math.sqrt((i[0] - robot[0])**2 + (i[1] - robot[1])**2)
        robot = i
    return distance


##########################################################################
# Write a function robot_lazy(l) that gets one argument: a list of
# apples l (each element is a pair of numbers). The robot is allowed to
# skip exactly one apple. Return the location of the apple which the
# robot will skip so that the total travelled distance will be minimum.
#
# Example: 
#
#     >>> robot_lazy([(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)])
#     (-2, -7)
#
# If the robot skip apple (-2, -7) then the total travelled distance is
# 30.003918305138853. If it skips any other apple then its path is longer.
##########################################################################
def robot_lazy(l):
    l_distance = []
    for i in range(1, len(l)+1):
        l_distance.append(robot_distance(l[:i-1]+l[i:]))

    for j in range(len(l_distance)):
        if l_distance[j] == min(l_distance):
            return l[j]


##########################################################################
# Write a function robot_smart(l) that gets one argument: a list of
# apples l. The function should return one number: the total distance
# travelled by the robot. This robot is smarter so the next apple it will
# pick is the one that is the closest to the robot. If there are many
# apples at the same distance from the robot, pick the one with smaller
# x-coordinate. If there are still many choices, pick the one with
# smaller y-coordinate. The starting location is (0, 0).
# 
# Example:
#
#     >>> robot_smart([(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)])
#     49.41812162728766
#
# The sequence of apples in the order they are collected:
#
#     (-1, 2), (1, 2), (3, 5), (-2, 12), (10, 10), (-2, -7)
##########################################################################
def robot_smart(l):
    dist = 0
    robot = (0, 0)

    for i in range(len(l)):
        dist_l = []
        for k in l:
            dist_l.append(math.sqrt((k[0] - robot[0]) ** 2 + (k[1] - robot[1]) ** 2))
        for j in range(len(dist_l)):
            if dist_l[j] == min(dist_l):
                dist += dist_l[j]
                robot = l[j]
                l.remove(l[j])
                break
    return dist


##########################################################################
# Write a function robot_optimal(l) that gets one argument: a list of
# apples l. The function should return one number: the total distance
# travelled by the robot. This robot is even smarter so it will pick
# apples in such a way that the total travelled distance is minimal.
#
# Example:
#
#     >>> robot_optimal([(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)])
#     42.70889663052099
#
# Hint: Is recursion your friend?
##########################################################################
def robot_optimal(l):
    all_l = list(permutations(l))
    all_dist = []
    for i in all_l:
        all_dist.append(robot_distance(i))
    return min(all_dist)

print(robot_optimal([(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)]))
##########################################################################
# === EXTRA TASK ===
#
# Write a function draw_apples(l) that draws the apples using turtle
# graphics. Each apple should be represented by a red circle. Also draw
# a line that represents the path of the "stupid" robot (from function
# robot_distance). Use scaling so that the closest two apples are at
# distance 30 on the drawing. (No two apples overlap.)
#
# Example: draw_apples([(1, 2), (-1, 2), (3, 5), (-2, -7), (-2, 12), (10, 10)])
# procudes the drawing on picture apples.png.
##########################################################################


