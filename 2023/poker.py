import random
import itertools

##########################################################################
# Producing a computer program that can play poker might be too ambitious
# project if you only have 3 hours. However, we will make a few helper
# functions that could be used in such software.
#
# Poker is played with a standard deck of 52 playing cards. Each card
# has a rank and a suit.
#
# Suits are: clubs (♣), diamonds (♦), hearts (♥), and spades (♠).
# We will denote them by letters C, D, H and S, respectively.
#
# Ranks are numbers 2 to 10, jack, queen, king and ace. To denote them
# we will use numbers 2 to 10, and letters J, Q, K and A, respectively.
##########################################################################

suits = ['C', 'D', 'H', 'S']
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] 

##########################################################################
# Each card will be repserented by a string which includes the card's
# suit and rank. For example, ace of diamond is 'AD', queen of spades is 'QS',
# ten of hears is '10H', five of clubs is '5C', etc.
#
# Write a function make_deck() that returns the list of all 52 cards.
# The cards in the deck should be randomly shuffled.
#
# Example:
#
#     >>> make_deck()
#     ['5S', '9D', '10D', 'AH', 'QD', '6H', ..., '7H', '8H', '7S', 'KD']
#     >>> make_deck()
#     ['JH', 'KC', '9H', '2C', 'QC', 'QD', ..., '8C', '8S', '9D', 'JC']
#
# Note: As the lists are long, some cards were erased and replaced by ...
# in the above examples.
##########################################################################

def make_deck():
    deck = []
    for s in suits:
        for r in ranks:
            deck.append(r + s)
    random.shuffle(deck)
    return deck

##########################################################################
# Write a function convert(card) that gets a string card that represents a card.
# The function should return a pair (r, s) where r is the rank of the card
# and s is its suit. For ranks 2 ... 10, r should be converted to an integer.
#
# Examples:
#
#     >>> convert('AD')
#     ('A', 'D')
#     >>> convert('5C')
#     (5, 'C')
#     >>> convert('10H')
#     (10, 'H')
#     >>> convert('QS')
#     ('Q', 'S')
##########################################################################
def convert(card):
    r, s = card[:-1], card[-1]
    if not (r in 'AKQJ'):
        r = int(r)
    return (r, s)


##########################################################################
# The hand of a player comprises 5 cards. If all cards are of the same
# suit, this is called a Flush. Write a function is_flush(hand), that
# gets a list of 5 cards and returns True if and only if the hand is a flush.
# 
# Examples:
#
#     >>> is_flush(['JH', 'KC', '9H', '2C', 'QC'])
#     False
#     >>> is_flush(['4D', 'KD', 'AD', '9D', '10D'])
#     True
##########################################################################

def is_flush(hand):
    l = []
    for c in hand:
        l.append(convert(c)[1])
    for x in l:
        if x != l[0]:
            return False
    return True

def is_flush(hand):
    l = []
    for c in hand:
        l.append(convert(c)[1])
    return len(set(l)) == 1

##########################################################################
# If the hand of a player consists of 5 cards of consecutive ranks, this is
# called a Straight. Ranks are ordered as follows:
#
#     A < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < A
#
# Ace might be either the highest or the lowest card, so A < 2 or K < A.
# Write a function is_straight(hand), that gets a list of 5 cards and
# returns True if and only if the hand is a straight. Beware of the ace!
# 
# Examples:
#
#     >>> is_straight(['JH', 'KC', '9H', '2C', 'QC'])
#     False
#     >>> is_straight(['6C', '4D', '8H', '5H', '7S'])
#     True
#     >>> is_straight(['2D', '4C', 'AD', '5C', '3S'])
#     True
#     >>> is_straight(['10H', 'KS', 'AC', 'JH', 'QD'])
#     True
##########################################################################

card_value = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def is_consecutive(hand):
    for i in range(1, len(hand)):
        if hand[i - 1] + 1 != hand[i]:
            return False
    return True

def is_straight(hand):
    l = []
    for c in hand:
        rank = convert(c)[0]
        rank = card_value.get(rank, rank)
        """
        if rank == 'J':
            rank = 11
        elif rank == 'Q':
            rank = 12
        elif rank == 'K':
            rank = 13
        elif rank == 'A':
            rank = 14
        """
        l.append(rank)
    l.sort()
    if is_consecutive(l):
        return True
    l2 = []
    for x in l:
        if x == 14:
            l2.append(1)
        else:
            l2.append(x)
    l2.sort()
    return is_consecutive(l2)


##########################################################################
# A very popular version of poker is the Texas hold 'em. There are 5 cards
# on the table and the player has 2 cards. The hand of the players is
# formed by 5 cards that maximise the ranking of player's hand. (We do not
# care about rankings here.)
#
# There are several ways to form the hand:
#
#     (a) both cards of the player + 3 cards from the table;
#     (b) one card of the player + 4 cards from the table;
#     (c) 5 cards from the table.
#
# Write a function all_hands(player, table) that gets two lists: list player
# contains the two cards of the player and list table contains 5 cards on
# the table. The function should return the list of all possible hands.
#
# Example:
#
#     >>> all_hands(['10D', 'AH'], ['QD', '7H', '8H', '7S', 'KD'])
#     [('10D', 'AH', 'QD', '7H', '8H'), ('10D', 'AH', 'QD', '7H', '7S'), 
#      ('10D', 'AH', 'QD', '7H', 'KD'), ('10D', 'AH', 'QD', '8H', '7S'), 
#      ('10D', 'AH', 'QD', '8H', 'KD'), ('10D', 'AH', 'QD', '7S', 'KD'), 
#      ('10D', 'AH', '7H', '8H', '7S'), ('10D', 'AH', '7H', '8H', 'KD'), 
#      ('10D', 'AH', '7H', '7S', 'KD'), ('10D', 'AH', '8H', '7S', 'KD'), 
#      ('10D', 'QD', '7H', '8H', '7S'), ('10D', 'QD', '7H', '8H', 'KD'), 
#      ('10D', 'QD', '7H', '7S', 'KD'), ('10D', 'QD', '8H', '7S', 'KD'), 
#      ('10D', '7H', '8H', '7S', 'KD'), ('AH', 'QD', '7H', '8H', '7S'), 
#      ('AH', 'QD', '7H', '8H', 'KD'), ('AH', 'QD', '7H', '7S', 'KD'), 
#      ('AH', 'QD', '8H', '7S', 'KD'), ('AH', '7H', '8H', '7S', 'KD'), 
#      ('QD', '7H', '8H', '7S', 'KD')]
##########################################################################
def all_hands(player, table):
    l = []  
    # Case (a)
    # i < j < k WLOG
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                hand = player + [table[i], table[j], table[k]]
                l.append(hand)
    # Case (b)
    for i in range(5):
        hand = [player[0]] + table[:i] + table[i+1:]
        l.append(hand)
        hand = [player[1]] + table[:i] + table[i+1:]
        l.append(hand)
    # Case (c)
    l.append(table)
    return l

def all_hands(player, table):
    l = []  
    all_card = player + table
    # i < j WLOG
    for i in range(7):
        for j in range(i + 1, 7):
            hand = all_card[:i] + all_card[i+1:j] + all_card[j+1:]
            l.append(hand)
    return l


def all_hands(player, table):
    return list(itertools.combinations(player + table, 5))

print(all_hands(['10D', 'AH'], ['QD', '7H', '8H', '7S', 'KD']))



