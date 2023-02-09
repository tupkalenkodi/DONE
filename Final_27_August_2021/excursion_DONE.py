##########################################################################
# Excursion 
#
# A group of people goes on an excursion. The list of participants is
# given as a list of strings which contain first and last names of the
# participants. A person may have more than one first name or more than
# one last name. In such a string last names are given first. This is
# followed by a comma and then all first names.
# 
# Example:
# 
#     participants = ['Miklavič, Janez Pavel', 'Miklavič, Jessica',
#                     'Kovač Miklavič, Mateja', 'Kovač, Boris']
#
# A helper function is provided below:
##########################################################################
participants = ['Miklavič, Janez Pavel', 'Miklavič, Jessica', 'Kovač Miklavič, Mateja', 'Kovač, Boris']
def first_and_last(s):
    '''
    Return a pair of string where the first string will only contain
    first names and the second string will only contain last names.
    '''
    s = s.split(',')
    return (s[1].strip(), s[0].strip())




##########################################################################
# They stop over for a lunch. They sit down in such a way that people with
# the same last names sit around the same table. Write a function
# table_arrangement(people) which will return a dictionary where keys are
# last names and their corresponding values are sets of first names of
# people with the given last name.
#
# Example:
# 
#     >>> table_arrangement(participants)
#     {'Miklavič': {'Jessica', 'Janez Pavel'}, 'Kovač': {'Boris'},
#      'Kovač Miklavič': {'Mateja'}}
##########################################################################
def table_arrangement(people):
    res_dict = {}
    for i in people:
        name_surname = first_and_last(i)
        res_dict[name_surname[1]] = set()
    for j in people:
        name_surname = first_and_last(j)
        res_dict[name_surname[1]].add(name_surname[0])

    return res_dict


##########################################################################
# We are looking for the most popular name in this group of people. If a
# person has more than one first name, each of them is counted separately.
# Write a function popular_name(people) that returns the list of popular
# names. The list should be sorted. The popular name is the one which is
# the most frequent. (There may be many popular names if all of them have
# the same frequency.)
#
# Example:
# 
#     >>> popular_name(['Horvat, Istvan Janez', 'Hočevar, Franc',
#                       'Horvat, Franc', 'Novak, Janez', 'Novak, Mateja'])
#     ['Franc', 'Janez']
##########################################################################
def popular_name(people):
    res_l = []
    return_l = []
    res_dict = {}
    for i in people:
        name = first_and_last(i)[0]
        for j in range(len(name)):
            if name[j] == ' ':
                res_l.append(name[:j])
                res_l.append(name[j+1:])
        res_l.append(name)
    for k in res_l:
        res_dict[k] = 0
    for n in res_l:
        res_dict[n] += 1

    max1 = max(res_dict.values())

    counter = 0
    for m in res_dict.values():
        if m == max1:
            return_l.append(list(res_dict.keys())[counter])
        counter += 1

    return return_l


##########################################################################
# Write a function maybe_relatives(person_1, person_2) which takes two
# strings and returns True if the two people can be relatives, i.e., if
# they have at least one last name in common. Otherwise the function
# should return False.
#
# Example:
# 
#     >>> maybe_relatives('Miklavič Novak, Franc', 'Novak, Mateja')
#     True
#     >>> maybe_relatives('Miklavič, Boris', 'Novak, Mateja')
#     False
##########################################################################
def maybe_relatives(person_1, person_2):
    surname1 = first_and_last(person_1)[1]
    surname2 = first_and_last(person_2)[1]
    res_surname1 = []
    res_surname2 = []

    counter = 0
    for i in range(len(surname1)):
        if surname1[i] == ' ':
            res_surname1.append(surname1[:i])
            res_surname1.append(surname1[i+1:])
            counter += 1
            break
    if counter == 0:
        res_surname1.append(surname1)

    counter = 0
    for j in range(len(surname2)):
        if surname2[j] == ' ':
            res_surname2.append(surname2[:j])
            res_surname2.append(surname2[j+1:])
            counter += 1
            break
    if counter == 0:
        res_surname2.append(surname2)

    for k in res_surname1:
        for l in res_surname2:
            if k == l:
                return True
                break
    return False


##########################################################################
# Write a function extended_family(person, people) which returns the list
# of those people (together with person) which may be related to the given
# person, i.e., relatives of the person, relatives of the relatives of the
# person, etc. The list should be sorted lexicographically.
# 
# Example:
#
#     >>> extended_family('A, x', ['A, a', 'A B, b', 'C D, c', 'C A, c', 'Y, x'])
#     ['A B, b', 'A, a', 'A, x', 'C A, c', 'C D, c']
##########################################################################
def extended_family(person, people):
    res_l = [person]
    for i in people:
        if maybe_relatives(person, i):
            res_l.append(i)
    res_l.sort()
    return res_l
