##########################################################################
# Sequences
##########################################################################

##########################################################################
# We will call a string a valid sequence of letters if there are no
# 4 consecutive characters in it which are the same. (It may, however,
# contain 3 consecutive characters which are the same.) Write a function
# is_valid(s) which takes a string and return True if it is a valid
# sequence of letters; or False otherwise.
#
# Example:
# 
#     >>> is_valid('aabbbcc')
#     True
#     >>> is_valid('aabbbbcc')
#     False
##########################################################################
def is_valid(s):
    res_dict = {}
    counter = 1
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
           counter += 1
           res_dict[s[i]] = counter
        elif s[i] != s[i+1]:
            counter = 1

    for i in res_dict.values():
        if i >= 4:
            return False

    return True


##########################################################################
# Write a function make_valid_sequences(n, s) that takes an integer n and
# a string s. Your function should return the list of all valid sequences
# of length n that only contain characters from the string s.
#
# Example:
# 
#     >>> make_valid_sequences(4, 'ab')
#     ['aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 
#      'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba']
#     >>> make_valid_sequences(6, 'abcd')
#     ['aaabaa', 'aaabab', 'aaabac', 'aaabad', 'aaabba', ...
# <<< There are 3936 sequences in total, most of which were omitted. >>>
#      ..., 'dddccd', 'dddcda', 'dddcdb', 'dddcdc', 'dddcdd']
##########################################################################

def make_sequences(n, s):
    if n == 1:
        seq1 = []
        for i in s:
            seq1.append(i)
        return set(seq1)
    shorter = make_valid_sequences(n - 1, s)
    seq = []
    for ss in shorter:
        for c in s:
            seq.append(c + ss)

    return seq


def make_valid_sequences(n, s):
    seq = make_sequences(n, s)
    res_seq = []
    for j in seq:
        if is_valid(j):
            res_seq.append(j)
    return res_seq


##########################################################################
# Write a function make_valid_limited(n, lims) that takes an integer n
# and a dictionary lims. Keys of dictionary lims are characters and values
# are integers. A character x may not appear more than lims[x] times in
# such a sequence. 
#
# Example:
#     >>> make_valid_limited(6, {'a': 2,'b': 2, 'c': 2, 'd': 1})
#     ['aabbcc', 'aabbcd', 'aabbdc', 'aabcbc', 'aabcbd', ...
# <<< There are 630 sequences in total, most of which were omitted. >>>
#      ..., 'dccaba', 'dccabb', 'dccbaa', 'dccbab', 'dccbba']
#      
#     >>> l = make_valid_limited(7, {'a': 5,'b': 5})
#     ['aaabaab', 'aaababa', 'aaababb', 'aaabbaa', 'aaabbab', 'aaabbba', ...
# <<< There are 86 sequences in total, most of which were omitted. >>>
#      ..., 'bbbaaab', 'bbbaaba', 'bbbaabb', 'bbbabaa', 'bbbabab', 'bbbabba']
##########################################################################
def test(s, lims):
    for i in s:
        pass

def make_valid_limited(n, lims):
    s = ''
    for i in list(lims.keys()):
        s += i
    all_seq = make_valid_sequences(n, s)

    res_seq = []
    for j in all_seq:
        dict_partial = {}
        for k in j:
            if k not in list(dict_partial.keys()):
                dict_partial[k] = 0
            dict_partial[k] += 1

        counter = 0
        for n in list(dict_partial.keys()):
            if dict_partial[n] > lims[n]:
                counter += 1
                break

        if counter == 0:
            res_seq.append(j)

    return res_seq


##########################################################################
# Two sequences are considered equivalent if one can be obtained from the
# other by a cyclic shift (of any length). For example 'cdaabb' can be
# obtained from 'aabbcd' by a cyclic shift of length 2.
#
# Write a function make_nonequivalent(n, s) that takes an integer n and
# a string s. Your function should return the list of all NON-EQUIVALENT
# valid sequences of length n that only contain characters from the string s.
# (You may include any sequence from the class of equivalent sequences.)
#
# Example:
# 
#     >>> make_nonequivalent(4, 'ab')
#     ['aaab', 'aabb', 'abab', 'abbb']
#
#     >>> make_nonequivalent(6, 'abcd')
#     ['aaabaa', 'aaabab', 'aaabac', 'aaabad', 'aaabba', ...
# <<< There are 696 sequences in total, most of which were omitted. >>>
#      ..., 'dcbddd', 'dccddd', 'ddaddd', 'ddbddd', 'ddcddd']
##########################################################################

def make_repr(seq_l):
    repr_seq = []
    l_comb = []
    for i in seq_l:
        l_comb = []
        for j in range(len(i) - 1, -1, -1):
            for k in range(len(i) - 1):
                i = i[j:] + i[:j]
                l_comb.append(i)
        l_comb.sort()
        repr_seq.append(l_comb[0])

    res_repr_seq = list(set(repr_seq))
    return res_repr_seq


def make_nonequivalent(n, s):
    all_seq = make_valid_sequences(n, s)
    res_l = make_repr(all_seq)
    res_l.sort()
    return res_l
