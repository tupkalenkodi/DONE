##########################################################################
# Words
##########################################################################

##########################################################################
# Command wc is a standard Unix command that return the number of lines,
# words, and characters in a file. A word is a maximal consecutive sequence
# of characters that does not contain spaces ' ', newlines '\n' or
# tabs '\t'. (This command has nothing to do with toilets.)
#
#     $ wc words_DONE.py
#      115  492 3461 words_DONE.py
#
# Note: The command was called before the file words_DONE.py was modified.
#
# Write a function wc(file_name) in that will get a name of a file and
# return a tuple with the three numbers.
#
# Example:
#
#     >>> wc('words_DONE.py')
#     (115, 492, 3461)
##########################################################################
def wc(file_name):
    f = open(file_name, 'r')
    number_lines = 0
    number_words = 0
    number_char = 0
    while True:
        line = f.readline()
        if line == '':
           break
        else:
           number_lines += 1

        number_words += len(line.strip().split())

        for j in line:
            number_char += 1

    return number_lines, number_words, number_char


##########################################################################
# Write a function sort_lines(in_file, out_file) that will get names of
# two files. The function should read words from the file in_file. There
# will be exactly one word in each line. The function should sort the
# words in lexicographic order and output them in the file out_file.
#
# Example:
#
#     >>> sort_lines('words.txt', 'words2.txt')
#
# Suppose that the file words.txt has the following content:
#
#     guava
#     lemon
#     cherry
#     fig
#     lime
#     apple
#     kiwi
#     banana
#
# The the resulting file words2.txt should have the following content:
#
#     apple
#     banana
#     cherry
#     fig
#     guava
#     kiwi
#     lemon
#     lime
##########################################################################
def sort_lines(in_file, out_file):
    f = open(in_file, 'r')
    g = open(out_file, 'w')
    l_words = []

    while True:
        line = f.readline()
        if line == '\n':
            continue
        if line == '':
            break
        else:
           l_words.append(line.strip())

    print(l_words)

    f.close()
    l_words.sort()
    for i in l_words:
        print(i, file=g)
    g.close()


##########################################################################
# Write a function mark_lines(in_file, out_file) that will get names of
# two files. The function should read words from the file in_file. There
# will be exactly one word in each line. The function should output the
# words to the file out_file in the same order as they appear in the in_file,
# but it should also prepend a number to the beginning of each line, i.e.
# the position of the word in the sorted file.
#
# Example:
#
#     >>> mark_lines('words.txt', 'words3.txt')
#
# If the file words.txt has the same content as above, the resulting file
# words3.txt will have the following content:
# 
#       5: guava
#       7: lemon
#       3: cherry
#       4: fig
#       8: lime
#       1: apple
#       6: kiwi
#       2: banana
##########################################################################
def mark_lines(in_file, out_file):
    f = open(in_file, 'r')
    g = open(out_file, 'w')
    l_words = []

    while True:
        line = f.readline()
        if line == '\n':
            continue
        if line == '':
            break
        else:
           l_words.append(line.strip())
    l_words_sort = l_words.copy()
    l_words_sort.sort()


    for j in l_words:
        counter = 1
        for k in l_words_sort:
            if j == k:
                print('{0}: {1}'.format(counter, j), file=g)
            else:
                counter += 1
    g.close()


##########################################################################
# Write a function reversed_lines(in_file, out_file) that will get names
# of two files. The function should read words from the file in_file.
# There will be exactly one word in each line. The function should output
# the reversed word followed by a space and the original word to the
# file out_file. The lines should be sorted with respect to the reversed
# words.
# 
# Example:
#
#     >>> reversed_lines('words.txt', 'words4.txt')
#
# If the file words.txt has the same content as above, the resulting file
# words4.txt will have the following content:
# 
#     ananab banana
#     avaug guava
#     elppa apple
#     emil lime
#     gif fig
#     iwik kiwi
#     nomel lemon
#     yrrehc cherry
##########################################################################
def reversed_lines(in_file, out_file):
    f = open(in_file, 'r')
    g = open(out_file, 'w')
    l_words = []

    while True:
        line = f.readline()
        if line == '\n':
            continue
        if line == '':
            break
        else:
           l_words.append(line.strip())

    l_words_reversed = []
    for i in l_words:
        k = i[::-1]
        l_words_reversed.append(k)

    l_words_reversed.sort()
    for n in range(len(l_words_reversed)):
        l_words[n] = l_words_reversed[n][::-1]

    for j in range(len(l_words)):
        print('{0} {1}'.format(l_words_reversed[j], l_words[j]), file=g)
    g.close()

