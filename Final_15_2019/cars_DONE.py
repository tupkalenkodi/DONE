##########################################################################
# Used Cars
#
# Stanko is buying used cars. He collected some data and stored it in a
# file. The data looks like this:
#
#     BMW_645Ci 2004 204.000 11.600
#     Golf_1.9TDI 2001 265000 650,00
#     Golf_1.9TDI 2008 269.000 6.250,00
#     Opel_Zafira 2006 230000 4000,00
#     Audi_A4_Avant 2008 191.000 9.600
#
# Each line starts with the model of the car (it does NOT contain spaces),
# followed by the year in which the car was made. The next number is the
# distance the car already travelled (in km). The last line is the price
# of the car.
#
# The data above is slightly inconsistent. Sometimes the . (dot) is used
# to separate groups of 3 digits (so that the number is easier to read),
# but it is often missing. Note that the ',' (comma) above is used to
# separate the decimals from the integer part.
##########################################################################

##########################################################################
# Write a function read_number(s) that takes a string s as its only
# argument. Strings s may contain digits, comma and dot. If the string
# contains a comma, then the function should return the float value that
# is represented by the string. If the string does not contain a comma,
# then the function should return the integer value that is represented
# by the string. If there are two or more commas, the function should
# return None.
#
# Examples:
# 
#     >>> read_number('269.000')
#     269000
#     >>> read_number('269.000,0')
#     269000.0
#     >>> read_number('269000,0')
#     read_number('269000,0')
#     >>> print(read_number('269,000,0'))
#     None
#     >>> read_number('1.269.000')
#     1269000
##########################################################################

def read_number(s):
    dict_sign = {'.': 0, ',': 0}
    proper_number = ''
    for char in s:
        if char == '.':
            dict_sign['.'] += 1
        elif char == ',':
            dict_sign[','] += 1
            proper_number += '.'
        else:
            proper_number += char

    if dict_sign[','] == 0:
        return int(proper_number)
    elif dict_sign[','] == 1:
        return float(proper_number)
    return None


##########################################################################
# Write a function load_data(file_name) that takes a name of a file which
# contains data as described above. The function should return a list of
# tuples. There should be one tuple for each line in the file (see example).
# The first element of the tuple should be a string (model of the car) and
# the remaining 3 elements should be numbers.
# 
# Example (suppose that cars.txt contains the sample that is given above):
# 
#     >>> load_data('cars.txt')
#     [('BMW_645Ci', 2004, 204000, 11600),
#      ('Golf_1.9TDI', 2001, 265000, 650.0),
#      ('Golf_1.9TDI', 2008, 269000, 6250.0),
#      ('Opel_Zafira', 2006, 230000, 4000.0),
#      ('Audi_A4_Avant', 2008, 191000, 9600)]
##########################################################################

def load_data(file_name):
    f = open(file_name, 'r')
    res2_l = []
    for i in f.readlines():
        res_l = i.strip().split()
        for num in range(1, 4):
            res_l[num] = read_number(res_l[num])
        res2_l.append(tuple(res_l))

    f.close()
    return res2_l


##########################################################################
# Stanko often wants to group together cars based on the year in which
# they were produced. Write a function group_cars(data) that will take
# a list of tuples (that represent used cars) and return a dictionary
# where keys are years and values are list of cars.
#
# Example:
#
#     >>> group_cars(load_data('cars.txt'))
#     {2004: [('BMW_645Ci', 2004, 204000, 11600)],
#      2001: [('Golf_1.9TDI', 2001, 265000, 650.0)],
#      2008: [('Golf_1.9TDI', 2008, 269000, 6250.0), ('Audi_A4_Avant', 2008, 191000, 9600)],
#      2006: [('Opel_Zafira', 2006, 230000, 4000.0)]}
##########################################################################

def group_cars(data):
    res_dict = {}
    for i in data:
        if i[1] not in list(res_dict.keys()):
            res_dict[i[1]] = []
        res_dict[i[1]].append(i)

    return res_dict


##########################################################################
# Write a function average_in_year(data) that will take a list of tuples
# (that represent used cars) and return a dictionary where keys are years
# and values pairs (avg_km, avg_price), where avg_km is the average number
# of kilometres travelled by cars made in that year; avg_price is the
# average price of those cars.
#
# Example:
#
#     >>> average_in_year(load_data('cars.txt'))
#     {2004: (204000.0, 11600.0), 2001: (265000.0, 650.0),
#      2008: (230000.0, 7925.0), 2006: (230000.0, 4000.0)}
##########################################################################

def average_in_year(data):
    partial_dict = group_cars(data)
    res_dict = {}

    for i in list(partial_dict.keys()):
        sum_dist = []
        sum_price = []
        for j in partial_dict[i]:
            sum_dist.append(j[2])
            sum_price.append(j[3])
        res_dict[i] = (sum(sum_dist) / len(sum_dist), sum(sum_price) / len(sum_price))

    return res_dict


##########################################################################
# Stanko wants to save his data to a file that is formatted as the one
# described above. Stanko wants the cars sorted by the year in which
# they were made (the youngest cars first). If there are multiple cars
# made in the same year, then they should be sorted by the price (cheaper
# cars first).
#
# Write a function save_data(data, file_name) that will take two arguments:
# a list of tuples (that represent used cars) and a file name. The function
# should print the data to this file. The data should be sorted as required
# by Stanko.
#
# Example:
#
#     >>> save_data(load_data('cars.txt'), 'cars_sorted.txt')
#
# The file cars_sorted.txt should contain:
#
#     Golf_1.9TDI 2008 269000 6250.0
#     Audi_A4_Avant 2008 191000 9600
#     Opel_Zafira 2006 230000 4000.0
#     BMW_645Ci 2004 204000 11600
#     Golf_1.9TDI 2001 265000 650.0
##########################################################################

def save_data(data, file_name):
    g = open(file_name, 'w')
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j][1] < data[j+1][1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
            elif data[j][1] == data[j+1][1]:
                if data[j][3] > data[j+1][3]:
                    tmp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = tmp

    for line in data:
        print(*list(line), file=g)
    g.close()
