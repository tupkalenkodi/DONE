##########################################################################
# Tic-tac-toe
#
# Tic-tac-toe is a paper-and-pencil game for two players, who take turns
# marking the spaces in a $3 \times 3$ grid. The first player uses 'X' and
# the second player uses 'O'. The player who succeeds in placing three
# of their marks in a horizontal, vertical, or diagonal row wins the game.
# 
# We will create the TicTacToe class and implement several functions.
# (However, we will NOT create an AI to play the game.)
##########################################################################



##########################################################################
# Create a constructor (method __init__) in the class that will get 3
# string (consisting of letters 'X', 'O' and ' ') that represent a state
# in the game.
#
# Example:
# 
#     >>> t = TicTacToe('XO ', ' X ', 'O  ')
#
# Moreover, the constructor should raise the ValueError if the arguments
# of the constructor do not represent a valid state of the game:
# 
#   * Each of the 3 string must be of length 3.
#   * The strings may only contain characters 'X', 'O' and ' '.
#   * Players take turns in placing 'X' and 'O' so: (a) the number of 'X's
#     equals the number of 'O's or (b) the number of 'X's is 1 more than
#     the number of 'O's.
##########################################################################

class TicTacToe:
    
    def __init__(self, first_r, second_r, third_r):
        # Check if all parameters are strings and have length of 3.
        if len(first_r) != 3 or type(first_r) != str or len(second_r) != 3 or type(second_r) != str or len(third_r) != 3 or type(third_r) != str:
            print("All parameters have to be strings of length 3.")

        # Define two variables for future comparison of numbers of X and O.
        counter_X = 0
        counter_O = 0

        # Check if the first row contains any other than 'X', 'O', ' ' characters.
        for i in first_r:
            if i != 'X' and i != 'O' and i != ' ':
                print("All rows can only contain 'X' 'O' ' '.")

            # Counter 'X', and 'O' in the first row.
            elif i == 'X':
                counter_X += 1
            elif i == 'O':
                counter_O += 1

        # Check if the second row contains any other than 'X', 'O', ' ' characters.
        for j in second_r:
            if j != 'X' and j != 'O' and j != ' ':
                print("All rows can only contain 'X' 'O' ' '..")

            # Counter 'X', and 'O' in the second row.
            elif j == 'X':
                counter_X += 1
            elif j == 'O':
                counter_O += 1

        # Check if the third row contains any other than 'X', 'O', ' ' characters.
        for k in third_r:
            if k != 'X' and k != 'O' and k != ' ':
                print("All rows can only contain 'X' 'O' ' '...")

            # Counter 'X', and 'O' in the third row.
            elif k == 'X':
                counter_X += 1
            elif k == 'O':
                counter_O += 1

        # Check if number of 'X' and 'O' differ more than in one point.
        if counter_O > counter_X:
            print("Number of X should be bigger or equal to number of O.")
        elif counter_X - counter_O > 1:
            print("Difference between number of X and O shouldn't exceed 1.")

        self.first_r = first_r
        self.second_r = second_r
        self.third_r = third_r


##########################################################################
# Write methods __str__ and __repr__ so that your class will work as is
# shown on the example below:
#
#     >>> t = TicTacToe('XO ', ' X ', 'O  ')
#     >>> t
#     TicTacToe('XO ', ' X ', 'O  ')
#     >>> print(t)
#      X | O |   
#     ---+---+---
#        | X |   
#     ---+---+---
#      O |   |   
##########################################################################

class TicTacToe(TicTacToe):
      def __repr__(self):
          return 'TicTacToe({0}, {1}, {2})'.format(self.first_r, self.second_r, self.third_r)

      def __str__(self):
          first = ' ' + self.first_r[0] + ' | ' + self.first_r[1] + ' | ' + self.first_r[2] + ' '
          second = ' ' + self.second_r[0] + ' | ' + self.second_r[1] + ' | ' + self.second_r[2] + ' '
          third = ' ' + self.third_r[0] + ' | ' + self.third_r[1] + ' | ' + self.third_r[2] + ' '
          hline = '---+---+---'
          return '{0}\n{1}\n{2}\n{1}\n{3}'.format(first, hline, second, third)


##########################################################################
# Write a method next_player that will return either 'X' or 'O' depending
# on which player should play next.
# 
# Example:
# 
#     >>> t = TicTacToe('XO ', ' X ', 'O  ')
#     >>> t.next_player()
#     'X'
##########################################################################
class TicTacToe(TicTacToe):
    def next_player(self):
        counter_X = 0
        counter_O = 0

        for i in self.first_r:
            if i == 'X':
                counter_X += 1
            elif i == 'O':
                counter_O += 1

        for j in self.second_r:
            if j == 'X':
                counter_X += 1
            elif j == 'O':
                counter_O += 1

        for k in self.third_r:
            if k == 'X':
                counter_X += 1
            elif k == 'O':
                counter_O += 1
        if counter_X == 0:
           return 'X'
        elif counter_O == counter_X:
            return 'X'
        else:
            return 'O'


##########################################################################
# Write a method winner that will return either 'X', 'O' or None.
# If some player has three of her marks in a horizontal, vertical, or
# diagonal row, she is the winner of the game. If there is no winner,
# the method should return None.
#
# Example:
# 
#     >>> t = TicTacToe('XO ', ' X ', 'O X')
#     >>> t.winner()
#     >>> 'X'
##########################################################################
class TicTacToe(TicTacToe):
      def winner(self):
          list_of_pos_X = []
          counter = 0
          for i in self.first_r:
              if i == 'X':
                  list_of_pos_X.append(counter)
              counter += 1
          counter = 3
          for i in self.second_r:
              if i == 'X':
                  list_of_pos_X.append(counter)
              counter += 1
          counter = 6
          for i in self.third_r:
              if i == 'X':
                  list_of_pos_X.append(counter)
              counter += 1

          list_of_pos_O = []
          counter = 0
          for i in self.first_r:
              if i == 'O':
                  list_of_pos_O.append(counter)
              counter += 1
          counter = 3
          for i in self.second_r:
              if i == 'O':
                  list_of_pos_O.append(counter)
              counter += 1
          counter = 6
          for i in self.third_r:
              if i == 'O':
                  list_of_pos_O.append(counter)
              counter += 1

          if [0,1,2] == list_of_pos_X or [3,4,5] == list_of_pos_X or [6,7,8] == list_of_pos_X:
              return 'X'
          elif [0,3,6] == list_of_pos_X or [1,4,7] == list_of_pos_X or [2,5,8] == list_of_pos_X:
              return 'X'
          elif [0,4,8] == list_of_pos_X or [2,4,6] == list_of_pos_X:
              return 'X'

          elif [0,1,2] == list_of_pos_O or [3,4,5] == list_of_pos_O or [6,7,8] == list_of_pos_O:
              return 'O'
          elif [0,3,6] == list_of_pos_O or [1,4,7] == list_of_pos_O or [2,5,8] == list_of_pos_O:
              return 'O'
          elif [0,4,8] == list_of_pos_O or [2,4,6] == list_of_pos_O:
              return 'O'
          else:
              return None


##########################################################################
# Write a method rotated that will return a new object of class TicTacToe
# that is obtained from the current object by rotating the grid by 90° in
# the clockwise direction.
#
# Example:
# 
#     >>> t = TicTacToe('XO ', ' X ', 'O  ')
#     >>> t.rotated()
#     >>> TicTacToe('O X', ' XO', '   ')
##########################################################################
class TicTacToe(TicTacToe):
      def rotated(self):
           new_first = self.third_r[0] + self.second_r[0] + self.first_r[0]
           new_second = self.third_r[1] + self.second_r[1] + self.first_r[1]
           new_third = self.third_r[2] + self.second_r[2] + self.first_r[2]
           return TicTacToe(new_first, new_second, new_third)


##########################################################################
# Write a method mirrored that will return a new object of class TicTacToe
# that is obtained from the current object by taking the mirror image 
# about horizontal line.
#
# Example:
#
#     >>> t = TicTacToe('XO ', ' X ', 'O  ')
#     >>> t.mirrored()
#     >>> TicTacToe('O  ', ' X ', 'XO ')
##########################################################################

class TicTacToe(TicTacToe):
    def mirrored(self):
        new_first = self.third_r[0] + self.third_r[1] + self.third_r[2]
        new_second = self.second_r[0] + self.second_r[1] + self.second_r[2]
        new_third = self.first_r[0] + self.first_r[1] + self.first_r[2]
        return TicTacToe(new_first, new_second, new_third)


##########################################################################
# Write a method __eq__ that will return True if and only if the
# two given states in the game are equivalent, i.e. one can be
# obtained from the other by any number of rotations and mirror images. 
#
# Example:
#
#     >>> t = TicTacToe('XO ', ' X ', 'O  ')
#     >>> u = TicTacToe('   ', ' XO', 'O X')
#     >>> t == u
#     True
##########################################################################
class TicTacToe(TicTacToe):
      def __eq__(self, other):
          if self.first_r == other.first_r and self.second_r == other.second_r and self.third_r == other.third_r:
              return True
          a = self.mirrored()
          if a.first_r == other.first_r and a.second_r == other.second_r and a.third_r == other.third_r:
              return True

          b = self.rotated()
          if b.first_r == other.first_r and b.second_r == other.second_r and b.third_r == other.third_r:
              return True
          c = b.mirrored()
          if c.first_r == other.first_r and c.second_r == other.second_r and c.third_r == other.third_r:
              return True

          d = b.rotated()
          if d.first_r == other.first_r and d.second_r == other.second_r and d.third_r == other.third_r:
              return True
          c = d.mirrored()
          if c.first_r == other.first_r and c.second_r == other.second_r and c.third_r == other.third_r:
              return True

          g = d.rotated()
          if g.first_r == other.first_r and g.second_r == other.second_r and g.third_r == other.third_r:
              return True
          c = d.mirrored()
          if c.first_r == other.first_r and c.second_r == other.second_r and c.third_r == other.third_r:
              return True

          else:
             return False

