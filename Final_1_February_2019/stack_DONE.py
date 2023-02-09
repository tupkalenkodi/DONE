##########################################################################
# Stack
#
# A (partial) implementation of the class Stack is already provided below
# (see the code). The stack is very similar to a list; this is why the
# constructor takes a list and stores it internally as an attribute called
# elements. 
# 
# Example:
#
#     >>> s = Stack([1, 2, 3])
#     >>> print(s)
#     BOTTOM | 1, 2, 3 < TOP
#
# As you already know, you are able to access (and modify) any element of
# a list in Python. This is not the case if you are dealing with a stack.
# You are only able to:
#
#  (a) add an element at the top; and
#  (b) remove an element from the top.
#
# Suppose that you have 3 books stacked on top of each other. If you were
# not strong enough to pick up 2 or more books at the same time, then you
# would have to remove the book at the top first in order to be able to
# access the one in the middle. Stack works in a similar way.
##########################################################################

class Stack:
    def __init__(self, ls):
        self.elements = ls[:]

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return 'BOTTOM | ' + str(self.elements)[1:-1] + ' < TOP'

    def __repr__(self):
        return 'Stack({0})'.format(self.elements)


##########################################################################
# Extend the class Stack by adding a new method called insert that only
# takes one argument, i.e. the element that is going to be added at the
# top of the stack.
#
# Example:
#
#     >>> s = Stack([1, 2, 3])
#     >>> s.insert(10)
#     >>> s.insert(20)
#     >>> print(s)
#     BOTTOM | 1, 2, 3, 10, 20 < TOP
##########################################################################

class Stack(Stack):
    def insert(self, element):
        self.elements.append(element)


##########################################################################
# Extend the class Stack by adding a new method called pop that takes no
# arguments does two things: (a) it returns the element at the top and
# at the same time (b) it removes this element from the stack.
#
# Example:
#
#     >>> s = Stack([1, 2, 3])
#     >>> s.pop()
#     3
#     >>> print(s)
#     BOTTOM | 1, 2 < TOP
##########################################################################

class Stack(Stack):
    def pop(self):
        el = self.elements[len(self.elements) - 1]
        self.elements.pop()
        return el


##########################################################################
# Write a function (it should be defined outside the class!!!) called
# valid_brackets(s) that takes a string s which may contain the following
# characters: '(', ')', '[', ']', '{', and '}'. The function should return
# True if the string is a valid expression, and False otherwise.
#
# Use the following strategy: Process the string from left to right.
#
#   (i) If the current character is '(', '[', or '{' then just insert
#       it on the stack.
#
#  (ii) If the current character is ')', ']', or '}' then check the
#       character that is located at the top of the stack. If it does
#       not match the current character (or if the stack is empty) then
#       we have just found an error.
#
# What should be on the stack after the string is processed?
#       
# Examples:
#
#     >>> valid_brackets('({[]([]{})}()[()])')
#     True
#     >>> valid_brackets('({[([]{})}()()])')
#     False
#     >>> valid_brackets('({[]([]{})}()[()')
#     False
##########################################################################

def valid_brackets(s):
    dict_char = {'(': ')', '[': ']', '{': '}'}
    stack = Stack([])
    for char in s:
        if char in list(dict_char.keys()):
            stack.insert(char)
        elif char in list(dict_char.values()):
            if char == dict_char[stack.elements[len(stack) - 1]]:
                stack.pop()
            else:
                return False
        else:
            print("Your sequence contains wrong characters(not in dict_char).")
            return False
    if len(stack) == 0:
        return True
    else:
        return False


##########################################################################
# === EXTRA TASK ===
#
# Write a function called fix_expression(s) that takes a string s which
# may contain the following characters: '(', ')', '[', ']', '{', and '}'.
# The function should return a valid expression that is obtained by fixing
# errors in s. Use the strategy described above. 
#
# If an error is detected then insert a new character to the string which
# matches the current closing bracket. What do you need to do at the end
# if the stack is not empty??
#
# Examples:
#
#     >>> fix_expression('({[](]})')
#     '({[]([]{})})'
#     >>> fix_expression('([]{})')
#     '([]{})'
#     >>> fix_expression('({[]([]{})}()[()')
#     '({[]([]{})}()[()])'
#     >>> fix_expression(')]}[{(')
#     '()[]{}[{()}]'
##########################################################################

def fix_expression(s):
    dict_char = {'(': ')', '[': ']', '{': '}'}
    dict_char_reverse = {')': '(', ']': '[', '}': '{'}
    stack = Stack([])
    new_s = ''
    for char in s:

        if char in list(dict_char.keys()):
            stack.insert(char)
            new_s += char
        elif char in list(dict_char.values()):
            if len(stack) != 0:
                if char == dict_char[stack.elements[len(stack) - 1]]:
                    new_s += char
                    stack.pop()
            else:
                new_s += dict_char_reverse[char]
                new_s += char
        else:
            print("Your sequence contains wrong characters(not in dict_char).")
            return False
    if len(stack) == 0:
        return new_s
    else:
        for c in reversed(stack.elements):
            new_s += dict_char[c]
        return new_s
