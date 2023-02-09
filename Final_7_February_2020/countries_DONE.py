##########################################################################
# Countries and languages
#
# In the dictionary below keys are names of countries and values are
# list of languages that are spoken in those countries.
##########################################################################

countries_example = {
    'Belgium': ['Dutch', 'French', 'German'],
    'Canada': ['English', 'French'],
    'Chile': ['Spanish'],
    'China': ['Chinese'],
    'Egypt': ['Arabic', 'English', 'French'],
    'Germany': ['German'],
    'India': ['Hindi', 'English', 'Bengali', 'Gujarati', 'Kashmiri', 'Punjabi', 'Tamil',
              'Telugu', 'Urdu', 'Sanskrit', 'Sindhi'],
    'Iran': ['Persian', 'Kurdish'], 
    'Italy': ['Italian'],
    'Kazakhstan': ['Kazak', 'Russian'],
    'Netherlands': ['Dutch', 'Frisian'],
    'Russia': ['Russian'],
    'Rwanda': ['Kinyarwanda', 'French', 'English'],
    'Seychelles': ['English', 'French'],
    'Switzerland': ['German', 'French', 'Italian'],
    'Taiwan': ['Chinese'],
    'UK': ['English', 'Welsh', 'Gaelic'],
    'USA': ['English', 'Spanish']
}

##########################################################################
# Write a function save_data(countries, file_name) that gets two arguments
# the first argument is the dictionary with data on countries (see above),
# and the second argument is a name of a file. The function should print
# the following data to the file:
#
#  * the first line should contain the number of countries;
#  * for each country print two lines:
#     - the first one contains the name of the country,
#     - the second line is a list of languages, separated by '; ' (semicolon
#       followed by a space).
#
# Example:
#
#     >>> save_data(countries_example, 'languages.txt')
#
# The first 11 line of file languages.txt are:
#
#     18
#     Belgium
#     Dutch; French; German
#     Canada
#     English; French
#     Chile
#     Spanish
#     China
#     Chinese
#     Egypt
#     Arabic; English; French
##########################################################################


def save_data(countries, file_name):
    f = open(file_name, 'w')
    keys = list(countries.keys())
    values = list(countries.values())
    print(len(values), file=f)
    for i in range(len(values)):
        print(keys[i], file=f)
        print(*values[i], sep='; ', file=f)

    f.close()


##########################################################################
# Write a function to_languages(countries) that gets a dictionary with
# countries (see example above). The function should return a new dictionary
# where keys are languages and values are lists of countries that speak
# that language.
#
# Example:
# 
#     >>> to_languages(countries_example)
#     {'Dutch': ['Belgium', 'Netherlands'],
#      'French': ['Belgium', 'Canada', 'Egypt', 'Rwanda', 'Seychelles', 'Switzerland'],
#      'German': ['Belgium', 'Germany', 'Switzerland'],
#      'English': ['Canada', 'Egypt', 'India', 'Rwanda', 'Seychelles', 'UK', 'USA'],
#      'Spanish': ['Chile', 'USA'], 
#      'Chinese': ['China', 'Taiwan'], 
#          <<< SEVERAL ENTRIES WERE OMITTED TO SAVE SPACE :-) >>> 
#      'Welsh': ['UK'], 
#      'Gaelic': ['UK']}
##########################################################################
def to_languages(countries):
    new_dict = {}
    keys = list(countries.keys())
    values = list(countries.values())

    for i in values:
        for j in i:
            if j not in new_dict:
                new_dict[j] = []

    for k in keys:
        for m in list(new_dict.keys()):
            if m in countries[k]:
                new_dict[m].append(k)

    return new_dict


##########################################################################
# Write a function lets_talk(countries) that gets a dictionary with
# countries. The function should return a new dictionary where keys are
# also countries and values are names of those other countries that have
# at least one language in common.
#
# Example:
#
#     >>> lets_talk(countries_example)
#     {'Belgium': ['Canada', 'Egypt', 'Germany', 'Netherlands', 'Rwanda', 'Seychelles', 'Switzerland'],
#      'Canada': ['Belgium', 'Egypt', 'India', 'Rwanda', 'Seychelles', 'Switzerland', 'UK', 'USA'], 
#      'Chile': ['USA'], 
#      'China': ['Taiwan'], 
#          <<< SEVERAL ENTRIES WERE OMITTED TO SAVE SPACE :-) >>> 
#      'UK': ['Canada', 'Egypt', 'India', 'Rwanda', 'Seychelles', 'USA'], 
#      'USA': ['Canada', 'Chile', 'Egypt', 'India', 'Rwanda', 'Seychelles', 'UK']}
##########################################################################
def lets_talk(countries):
    new_dict = {}
    res_dict = {}

    for i in list(countries.keys()):
        new_dict[i] = []
    for j in list(to_languages(countries).values()):
        for k in j:
            new_dict[k] += j

    keys = list(new_dict.keys())
    for n in keys:
        l_countries = list(set(new_dict[n]))
        l_countries.remove(n)
        if l_countries:
            res_dict[n] = sorted(l_countries)

    return res_dict


##########################################################################
# Two countries, c_1 and c_2, have a diplomatic dispute, and they refuse
# to talk to each other (even if they speak a common language). Write
# a function mediators(countries, c_1, c_2) that will find a list of
# countries that can serve as a mediator in the dispute. A mediator should
# have at least one language in common with c_1 and at least one language
# in common with c_2.
#
# Example:
#
#     >>> mediators(countries_example, 'USA', 'Canada')
#     ['Egypt', 'India', 'Rwanda', 'Seychelles', 'UK']
#     >>> mediators(countries_example, 'Belgium', 'Germany')
#     ['Switzerland']
#     >>> mediators(countries_example, 'Iran', 'USA')
#     []
##########################################################################
def mediators(countries, c_1, c_2):
    if c_1 in lets_talk(countries).keys():
        l_1 = lets_talk(countries)[c_1]
    else:
        return []

    if c_2 in lets_talk(countries).keys():
        l_2 = lets_talk(countries)[c_2]
    else:
        return []

    res_l = []
    for i in l_1:
        if i in l_2:
            res_l.append(i)

    return res_l
