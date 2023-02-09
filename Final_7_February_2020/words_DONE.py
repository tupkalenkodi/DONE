##########################################################################
# Words
#
# A famous poet, let us call him Russ, sometimes has troubles finding
# appropriate words for his poems (e.g. words that rhyme with certain
# other words). We will help him out.
#
# A function load_words(file_name) is already provided. It is used in
# several examples. A file words.txt which contains 9894 words in English
# is also provided.
##########################################################################
def load_words(file_name):
	"""
	Return a list of words that are written in file file_name
	(one per line).
	"""
	with open(file_name) as f:
		return [word.strip() for word in f]


##########################################################################
# Write a function rhyme(l, suffix) that gets two arguments: a list of
# words l and a string suffix. This function should return a new list that
# contains all words from l that have the given suffix (i.e. ending).
# Words that are not at least len(suffix) characters long should be ignored.
#
# Examples:
#
#     >>> rhyme(['travelers', 'basement', 'textile', 'succeed', 'settlement'], 'ment')
#     ['basement', 'settlement']
#     >>> rhyme(load_words('words.txt'), 'fication')
#     ['certification', 'classification', 'identification', 'modification', 
#      'notification', 'qualification', 'specification', 'verification']
##########################################################################
def rhyme(l, suffix):
	res_l = []
	for i in l:
		if (len(i) >= len(suffix)) and (suffix in i) and (i[len(i) - 1] == suffix[len(suffix) - 1]):
			res_l.append(i)
	return res_l


##########################################################################
# Write a function poet_sorted(l) that get one argument: a list of strings
# l. The function should return a new list of strings that contains all
# elements of l, but they have to be sorted lexicographically with respect
# to their reverses.
#
# For example, the word 'taiwan' come before 'butler', because the reverse
# of 'taiwan' is 'nawiat', the reverse of 'butler' is 'reltub', and
# 'nawiat' < 'reltub'.
#
# Example:
#
#     >>> poet_sorted(['routes', 'thinking', 'item', 'qualify', 'ruby', 'butler', 'taiwan'])
#     ['thinking', 'item', 'taiwan', 'butler', 'routes', 'ruby', 'qualify']
##########################################################################
def poet_sorted(l):
	reverse_l = []
	res_l = []
	for i in l:
		reverse_l.append(i[::-1])
	reverse_l.sort()
	for j in reverse_l:
		res_l.append(j[::-1])
	return res_l


##########################################################################
# Write a function largest_prefix_group(n, l) that gets two argument: an
# integer n, and a list of strings l. The function should return a new
# list: the largest group of strings that have the same prefix (beginning)
# of length n. Words that are not at least n characters long should be
# ignored.
#
# If there is more than one possible solution, your function can
# return any of them. (You can assume that the longest strings in l is at
# least n characters long.)
#
# Example:
#
#     >>> largest_prefix_group(6, load_words('words.txt'))
#     ['organic', 'organisation', 'organisations', 'organised', 'organisms',
#      'organization', 'organizational', 'organizations', 'organize',
#      'organized', 'organizer', 'organizing']
#
# In the above example the solution is not unique. Two alternative groups
# that also contain 12 words are:
#
#     ['produce', 'produced', 'producer', 'producers', 'produces',
#      'producing', 'product', 'production', 'productions', 'productive',
#      'productivity', 'products']
#
# and
#
#     ['invest', 'investigate', 'investigated', 'investigation',
#      'investigations', 'investigator', 'investigators', 'investing',
#      'investment', 'investments', 'investor', 'investors']
##########################################################################
def largest_prefix_group(n, l):
	l_prefixes = []
	for i in l:
		if len(i) >= n:
			l_prefixes.append(i[:n])

	dict_prefixes = {}
	for j in l_prefixes:
		dict_prefixes[j] = []
		for k in l:
			if k[:n] == j:
				dict_prefixes[j].append(k)

	res = dict_prefixes[l_prefixes[0]]
	for n in range(len(dict_prefixes.values())):
		if len(res) < len(dict_prefixes[l_prefixes[n]]):
			res = dict_prefixes[l_prefixes[n]]
	return res


##########################################################################
# Write a function find_pair(word, l) that gets two argument: a string
# word, and a list of strings l. The function should find a pair of two
# words (w_1, w_2) that are cointained in l and have the following
# properties:
#
#  * w_1 and w_2 are both different from word;
#  * w_1 contains a prefix p_1 with the property 3 <= len(p_1) < len(w_1);
#  * w_2 contains a suffix p_2 with the property 3 <= len(p_2) < len(w_2);
#  * word is obtained by concatenating p_1 and p_2.
#
# If the solution is not unique your function can return any of them.
# If there is no solution your function should return None.
#
# Example:
#
#     >>> find_pair('prepared', load_words('words.txt'))
#     ('precious', 'compared')
#     >>> print(find_pair('prerequisite', load_words('words.txt'))
#     None
#
# In the first example the solution is far from unique. Some more
# possible pairs are ('prepaid', 'declared'), ('pregnancy', 'compared'),
# ('preparing', 'sacred'), ...
##########################################################################
def find_pair(word, l):
	l_w1 = []
	l_w2 = []
	for i in l:
		for j in range(3, len(word)):
			if i[:j] == word[:j] and len(i[:j]) < len(i) and i != word:
				l_w1.append(i)
				break

	for i in l:
		for j in range(3, len(word)):
			if i[j:] == word[j:] and len(i[j:]) >= 3 and i != word:
				l_w2.append(i)
				break


	for v in l_w1:
		for m in l_w2:
			for h in range(3, len(word)):
				if (v[:h] + m[h:]) == word:
					return (v,m)



##########################################################################
# === EXTRA TASK ===
#
# Create a new file named words_nopairs.txt that contains those words
# from words.txt for which there is no pair (w_1, w_2) as described in
# the previous task among the strings in words.txt.
#
# (It is believed that there are 4318 such words.)
##########################################################################
def nopairs(f, l):
	f = open(f, 'w')
	counter = 0
	for i in l:
		if find_pair(i, l) is None:
			counter += 1
	f.close()
	return counter


print(nopairs('a.txt', load_words('words.txt')))



