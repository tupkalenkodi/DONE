##########################################################################
# Drawing
#
# A function display_image(ascii_matrix) that prints an ASCII art image
# given by a matrix (where each element is a single character) is already
# provided. You can use this function for testing purposes and/or you can
# reuse its code in your own functions if you like.
##########################################################################

def display_image(ascii_matrix):
    """
    Prints an ASCII art image.
    """
    for line in ascii_matrix:
        print(''.join(line))


##########################################################################
# Write a function load_image(file_name) that gets a string file_name as
# its only argument. The function should open the file and load the ASCII
# art image. It should return the image in the form of a matrix where each
# element is a single character. You can assume that each line if the file
# contains the same number of characters.
#
# Example:
# 
#     >>> img = load_image('drawing01.txt')
#     >>> len(img)
#     15
#     >>> len(img[0])
#     32
#     >>> display_image(img)
#                                   __
#                          /\    .-" /
#                         /  ; .'  .'
#                        :   :/  .'
#                         \  ;-.'
#            .--""""--..__/     `.
#          .'           .'    `o  \
#         /                    `   ;
#        :                  \      :
#      .-;        -.         `.__.-'
#     :  ;          \     ,   ;
#     '._:           ;   :   (
#         \/  .__    ;    \   `-.
#          ;     "-,/_..--"`-..__)
#          '""--.._:
##########################################################################

def load_image(file_name):
    f = open(file_name, 'r')

    # For counting a number of lines in a file.
    with open(file_name, 'r') as g:
        counter = len(g.readlines())

    img = []
    for i in range(counter):
        line = f.readline()
        img.append([el for el in line[:len(line) - 1]])

    return img


##########################################################################
# Write a function draw_rectangle(image_matrix, r, c, h, w, char) that
# takes 6 arguments: image_matrix is a matrix with an ASCII art image,
# r, c, w and h are integers and char is a character. The function should
# draw a filled rectangle composed of characters char on the image. The
# height and width of the rectangle is h and w, respectively. Its upper
# left corner should be at (r, c). The function should not return anything,
# it should modify the matrix directly.
#
# Example:
#
#     >>> img = load_image('drawing01.txt')
#     >>> draw_rectangle(img, 3, 7, 5, 10, '@')
#     >>> display_image(img)
#                                   __
#                          /\    .-" /
#                         /  ; .'  .'
#            @@@@@@@@@@  :   :/  .'
#            @@@@@@@@@@   \  ;-.'
#            @@@@@@@@@@.__/     `.
#          .'@@@@@@@@@@ .'    `o  \
#         /  @@@@@@@@@@        `   ;
#        :                  \      :
#      .-;        -.         `.__.-'
#     :  ;          \     ,   ;
#     '._:           ;   :   (
#         \/  .__    ;    \   `-.
#          ;     "-,/_..--"`-..__)
#          '""--.._:
##########################################################################

def draw_rectangle(image_matrix, r, c, h, w, char):
    for i in range(h):
        for j in range(w):
            image_matrix[r+i][c+j] = char


##########################################################################
# Write a function save_image(image_matrix, file_name) that gets two
# arguments: a matrix with ASCII art image image_matrix and a string
# file_name. The function should print the image_matrix to a file named
# file_name.
#
# Example:
#
#     >>> img = load_image('drawing01.txt')
#     >>> draw_rectangle(img, 3, 7, 5, 10, '@')
#     >>> save_image(img, 'new_drawing.txt')
#
# The image from the previous task should now be saved in the file
# new_drawing.txt.
##########################################################################

def save_image(image_matrix, file_name):
    f = open(file_name, 'w')
    for line in image_matrix:
        print(''.join(line), file=f)


##########################################################################
# Write a function rectangles(h, w) that returns a new ASCII art image.
# The height of the image should be h and the width should be w. The image
# contains rectangles composed of characters '@' and '.' as you can see
# in the examples below.
#
# Examples:
#
#     >>> img_1 = rectangles(9, 5)
#     >>> display_image(img_1)
#     @@@@@
#     @...@
#     @.@.@
#     @.@.@
#     @.@.@
#     @.@.@
#     @.@.@
#     @...@
#     @@@@@
#     >>> img_2 = rectangles(10, 20)
#     >>> display_image(img_2)
#     @@@@@@@@@@@@@@@@@@@@
#     @..................@
#     @.@@@@@@@@@@@@@@@@.@
#     @.@..............@.@
#     @.@.@@@@@@@@@@@@.@.@
#     @.@.@@@@@@@@@@@@.@.@
#     @.@..............@.@
#     @.@@@@@@@@@@@@@@@@.@
#     @..................@
#     @@@@@@@@@@@@@@@@@@@@
##########################################################################
def rectangles(h, w):
    img = ['@' * w]

    j = 1
    sign = '.'
    for i in range(0, (h // 2) - 1):
        if i == 0 or i % 2 == 0 and len('@.' * (j+1) + sign * (w - 4*(j+1)) + (j+1) * '.@') <= w:
            sign = '.'
        else:
            sign = '@'

        img.append(['@.' * j + sign * (w - 4*j) + j * '.@'])
        if i % 2 == 1 and len('@.' * (j+1) + sign * (w - 4*(j+1)) + (j+1) * '.@') <= w:
            j += 1

        if i == (h // 2) - 2:
            img_2 = img.copy()
            img_2.reverse()

        if h % 2 == 1 and i == (h // 2) - 2:
            if i % 2 == 1 and len('@.' * (j + 1) + sign * (w - 4 * (j + 1)) + (j + 1) * '.@') <= w:
                j -= 1
            img.append(['@.' * j + sign * (w - 4 * j) + j * '.@'])

    return img + img_2
