##########################################################################
# Binary trees
#
# A binary tree is a data structure composed of several nodes. Each node
# contains some data (number) and may have up to two subtrees attached to
# it (the left and the right subtree). An example of a binary tree:
#
#
#            17
#           /  \
#          /    \
#         3      2
#          \    / \
#           4  8   1
#             / \
#            9   6
# 
# The class Tree for representing such trees is already implemented.
# The constructor takes three arguments: the number, the left subtree
# and the right subtree. If the subtree is empty, the corresponding
# values is None. (Those are also the default values of left and right.)
#
# Example (the above Tree can be constructed like this):
#
#     >>> t = Tree(17, left=Tree(3, right=Tree(4)), right=Tree(2,
#             left=Tree(8, left=Tree(9), right=Tree(6)), right=Tree(1)))
#     >>> t
#     Tree(17, left=Tree(3, right=Tree(4)), right=Tree(2, left=Tree(8,
#     left=Tree(9), right=Tree(6)), right=Tree(1)))
##########################################################################

class Tree:

	def __init__(self, n, left=None, right=None):
		self.n = n
		self.left = left
		self.right = right

	def __repr__(self):
		if self is None:
			return None
		l = '' if self.left is None else ', left={0}'.format(repr(self.left))
		r = '' if self.right is None else ', right={0}'.format(repr(self.right))
		return 'Tree({0}{1}{2})'.format(self.n, l, r)


##########################################################################
# Write a method add(x) that increases all numbers in the tree by x.
#
# Example:
#
#     >>> t = Tree(17, left=Tree(3, right=Tree(4)), right=Tree(2,
#             left=Tree(8, left=Tree(9), right=Tree(6)), right=Tree(1)))
#     >>> t.add(6)
#     >>> t
#     Tree(23, left=Tree(9, right=Tree(10)), right=Tree(8, left=Tree(14,
#     left=Tree(15), right=Tree(12)), right=Tree(7)))
# 
# Hint: Recursion is your best friend!
##########################################################################

class Tree(Tree):
	def add(self, x):
		if self.left is None and self.right is None:
			self.n += x
			return self
		else:
			if self.left is not None:
				left_0 = self.left
				left_0.add(x)
			else:
				left_0 = None

			if self.right is not None:
				right_0 = self.right
				right_0.add(x)
			else:
				right_0 = None

			self.n += x

			return Tree(self.n, left=left_0, right=right_0)


##########################################################################
# Write a method sum() that returns the sum of all numbers in the tree.
#
# Example:
#
#     >>> t = Tree(17, left=Tree(3, right=Tree(4)), right=Tree(2,
#             left=Tree(8, left=Tree(9), right=Tree(6)), right=Tree(1)))
#     >>> t.sum()
#     50
# 
# Hint: Recursion is your best friend!
##########################################################################

class Tree(Tree):
	def sum(self):
		if self.left is None and self.right is None:
			return self.n
		else:
			sum_num = self.n
			if self.left is not None:
				left_0 = self.left
				sum_num += left_0.sum()

			if self.right is not None:
				right_0 = self.right
				sum_num += right_0.sum()

			return sum_num


##########################################################################
# Write a method mirror() that creates and returns a new tree. In this new
# tree all left subtrees become right subtrees and vice versa.
#
# Example:
#
#     >>> t = Tree(17, left=Tree(3, right=Tree(4)), right=Tree(2,
#             left=Tree(8, left=Tree(9), right=Tree(6)), right=Tree(1)))
#     >>> t.mirror()
#     Tree(17, left=Tree(2, left=Tree(1), right=Tree(8, left=Tree(6),
#     right=Tree(9))), right=Tree(3, left=Tree(4)))
# 
# Hint: Recursion is your best friend!
##########################################################################

class Tree(Tree):
	def mirror(self):
		if self.left is None and self.right is None:
			return Tree(self.n)
		else:
			if self.left is not None:
				self.left = self.left.mirror()
			if self.right is not None:
				self.right = self.right.mirror()
			return Tree(self.n, left=self.right, right=self.left)


##########################################################################
# === EXTRA SUBTASK ===
#
# Write a method __str__() that returns a string that represents the
# tree as shown in the example below. The top value is printed immediately.
# The next few lines contain the left subtree. This is followed by the
# lines that contain the right subtree. Subtrees on each level are indented
# by 4 spaces. Empty subtrees should be represented by the '*' symbol.
#
# Example:
#
#     >>> t = Tree(17, left=Tree(3, right=Tree(4)), right=Tree(2,
#             left=Tree(8, left=Tree(9), right=Tree(6)), right=Tree(1)))
#     >>> print(t)
#     17
#         3
#             *
#             4
#         2
#             8
#                 9
#                 6
#             1
# 
# Note: Method __str__ is implicitly used by the print function.
##########################################################################


class Tree(Tree):

	pass
