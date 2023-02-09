##########################################################################
# Digrams
##########################################################################

##########################################################################
# Write a function find_digrams(s) that finds all digrams in the string s.
# Digrams are strings of length 2 that contain two consecutive letters.
# The function should return a list of strings where each string is of
# length 2 in lowercase. (See the example below.) 
#
# Example:
# 
#     >>> find_digrams('Danes je lep dan.')
#     ['da', 'an', 'ne', 'es', 'je', 'le', 'ep', 'da', 'an']
##########################################################################
def find_digrams(s):
    res_l = []
    for i in range(len(s) - 1):
        if s[i + 1] != ' ' and s[i + 1] != '.' and s[i] != ' ' and s[i] != '.':
           res_l.append(s[i:i+2].lower())
    return res_l


##########################################################################
# Write a function count_first(s) that gets a string s and determines
# frequencies of letters that are first letters of words in string s.
# The result should be returned in a form of a dictionary. All letters
# (keys of the dictionary) should be in lowercase.
#
# Example:
# 
#     >>> count_first('Danes je lep dan. Slovenščina je težka.')
#     {'d': 2, 'j': 2, 'l': 1, 's': 1, 't': 1}
##########################################################################
def count_first(s):
    res_dict = {}
    new_l = []
    memory = 0
    for i in range(len(s)):
            if s[i] == ' ':
                if s[memory:i] != '':
                    new_l.append(s[memory:i])
                    memory = i+1
            elif s[i] == '.':
                if s[memory:i] != '':
                    new_l.append(s[memory:i])
                    memory = i + 2

    for j in new_l:
        res_dict[j[0].lower()] = 0
    for k in new_l:
        res_dict[k[0].lower()] += 1
    return res_dict


##########################################################################
# Write a function count_digrams(s) that gets a string s and determines
# frequencies of all digrams in the string s. The result should be returned
# in a form of a dictionary. All digrams (keys of the dictionary) should
# be in lowercase.
#
# Example:
# 
#     >>> count_digrams('Danes je lep dan.')
#     {'da': 2, 'an': 2, 'ne': 1, 'es': 1, 'je': 1, 'le': 1, 'ep': 1}
#
# Hint: Use the function find_digrams(s).
##########################################################################
def count_digrams(s):
    new_l = find_digrams(s)
    res_dict = {}
    for i in new_l:
        res_dict[i] = 0
    for j in new_l:
        res_dict[j] += 1
    return  res_dict


##########################################################################
# Write a function digrams_table(s, file_name) which takes a string s
# and another string file_name. The function should find the frequencies
# of digrams in the string s and print them to a file named file_name in
# the form of a table as shown below. Digrams should be sorted alphabetically.
#
# After the function call:
# 
#     >>> digrams_table('Danes je lep dan.', 'digrams.txt')
#
# the file 'digrams.txt' should contain:
#
# Digram | Frequency
# -------+----------
#   an   |       2
#   da   |       2
#   ep   |       1
#   es   |       1
#   je   |       1
#   le   |       1
#   ne   |       1
##########################################################################
def digrams_table(s, file_name):
    f = open(file_name, "w")
    res_dict = count_digrams(s)

    keys = list(res_dict.keys())
    keys2 = list(res_dict.keys())
    keys2.sort()

    values = list(res_dict.values())

    counter = 0
    counter2 = 0
    for j in range(len(keys)):
        if keys[j] != keys2[j]:
            counter = j
            for i in range(len(keys2)):
                if keys[j] == keys2[i]:
                    counter2 = i
                    break
        else:
            counter = j
            counter2 = j

        tmp = values[counter]
        values[counter] = values[counter2]
        values[counter2] = tmp

    for i in range(len(keys)):
        print(keys2[i] + '   |       ' + str(values[i]), file= f)


digrams_table('Danes je lep dan.', 'digrams.txt')