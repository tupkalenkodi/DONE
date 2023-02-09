##########################################################################
# Keypad
# 
# Old fashioned mobile phones (ancestors of smartphones) usually had 12
# keys (digits from 0 to 9 and, in addition, characters '*' and '#')
# that were arranged in a $4 \times 3$ matrix. If you want to write an
# SMS on such a device, you may need to press some key more than once
# just to get a single letter. Letters are arranged on keys 2..9 in the
# following way:
# 
#               2: ABC    3: DEF
#     4: GHI    5: JKL    6: MNO
#     7: PQRS   8: TUV    9: WXYZ
# 
# If you want to input the letter 'N', you have to press key 6 twice. If
# you want to input the letter 'Z', you have to press key 9 for 4 times.
##########################################################################

##########################################################################
# Such a keypad can be represented with a list of the following type:
# 
#     >>> l = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
# 
# The first element represents letters on the key 2, the second element
# represents letters on the key 3, etc. But one may come up with a
# different arrangement of keys, for example:
#
#     >>> l = ['abcd', 'ef', 'gh', 'ijk', 'lmnop', 'qrst', 'uv', 'wxyz']
# 
# Write a function mobile_keys(l) that will take a list l as described
# above and return a dictionary, whose keys will be letters of the English
# alphabet and their corresponding values will be pairs of integers
# $(k, t)$, where k is the key that needs to be pressed and t is the
# number of hits that will produce the respective letter.
# 
# Example:
#
#     >>> mobile_keys(['abcd', 'ef', 'gh', 'ijk', 'lmnop', 'qrst', 'uv', 'wxyz'])
#     {'k': (5, 3), 'h': (4, 2), 'q': (7, 1), 'y': (9, 3), 'g': (4, 1), ... }
##########################################################################

def mobile_keys(l):
    res_dict = {}
    for i in range(len(l)):
        counter = 1
        for j in l[i]:
            res_dict[j] = (i+2, counter)
            counter += 1
    return res_dict


##########################################################################
# Write a function mobile_keys_inv(d) that will be an inverse function
# to mobile_keys, i.e. it will get a dictionary d as the argument and
# should return the list that represents the keypad.
# 
# Note: You can assume that the dictionary will represent a valid keypad.
# 
# Example:
# 
#     >>> mobile_keys_inv({'s': (7, 3), 'h': (4, 2), 'z': (9, 4), 'v': (8, 2),
#         'e': (3, 1), 't': (7, 4), 'i': (5, 1), 'p': (6, 5), 'x': (9, 2),
#         'f': (3, 2), 'l': (6, 1), 'q': (7, 1), 'd': (2, 4), 'c': (2, 3),
#         'u': (8, 1), 'n': (6, 3), 'j': (5, 2), 'w': (9, 1), 'm': (6, 2),
#         'o': (6, 4), 'a': (2, 1), 'y': (9, 3), 'b': (2, 2), 'k': (5, 3),
#         'r': (7, 2), 'g': (4, 1)})
#     ['abcd', 'ef', 'gh', 'ijk', 'lmnop', 'qrst', 'uv', 'wxyz']
##########################################################################

def mobile_keys_inv(d):
    res_list = ['', '', '', '', '', '', '', '']
    res_list2 = []
    for k in d.keys():
         res_list[d[k][0] - 2] += k
    for j in range(len(res_list)):
        k = list(res_list[j])
        k.sort()
        word = ''
        for i in k:
            word += i
        res_list2.append(word)
    return res_list2


##########################################################################
# Write a function key_count(l, sms) that will get a keypad l represented
# with a list (as described above) and a string sms that contains only
# lowercase letter of the English alphabet and spaces. The function should
# return the total number of key hits to type the sms.
#
# Note: The space is located on key 0, and you only need 1 hit.
#
# Example:
#
#     >>> key_count(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'],
#                   'we all live in a yellow submarine')
#     68
#
# We need 1 hit for 'w', 2 hits for 'e', 1 hit for ' ', 1 hit for 'a', ...
##########################################################################

def key_count(l, sms):
    number = 0
    dict = mobile_keys(l)
    for i in sms:
        if i != ' ':
            number += dict[i][1]
        else:
            number += 1
    return number


##########################################################################
# Write a function keypads(a, b) that will return a list of all possible
# keypads (represented by lists, as described above). Let k_i denote the
# number of letters on key i for i = 2,...,9. Then the following should
# hold:
#
#     * a <= k_i <= b for all i = 2,...,9
#     * k_2 + k_3 + ... + k_9 = 26
#     * Key 2 contains the first k_2 letters of the English alphabet,
#       key 3 contains the next k_3 letters, etc.
#
#     >>> keypads(3, 4)  
#     [['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stuv', 'wxyz'],
#      ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'],
#      ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuvw', 'xyz'],
#
#       ... (there are 28 keypads in total; 23 were omitted) ...
#
#      ['abcd', 'efg', 'hijk', 'lmn', 'opq', 'rst', 'uvw', 'xyz'],
#      ['abcd', 'efgh', 'ijk', 'lmn', 'opq', 'rst', 'uvw', 'xyz']]
##########################################################################

all_letters = 'abcdefghijklmnopqrstuvwxyz'
def keypads(a, b):
    all_number_combinations = split_number((), 26, 8, 3, 4)
    res_l = []
    for i in all_number_combinations:
        history = 0
        res_partial = []
        for j in i:
            res_partial.append(all_letters[history:history + int(j)])
            history = int(j)
        res_l.append(res_partial)

    return res_l


def split_number(p, n, k, a, b):
    if len(p) == k:
        if sum(p) == n:
            return [p]
        else:
            return []
    if sum(p) > n:
        return []
    res_l = []
    for x in range(1, n - sum(p) + 1):
        res_l.extend(split_number(p + (x,), n, k, a, b))
    for i in res_l:
        for j in i:
            if j < a or j > b:
                return []
    return res_l


def split_number2(p, n, k):
    if len(p) == k:
        if sum(p) == n:
            return [p]
        else:
            return []
    if sum(p) > n:
        return []
    l = []
    for x in range(1, n - sum(p) + 1):
        l.extend(split_number2(p + (x,), n, k))
    return l

print(split_number2((), 10, 3))
