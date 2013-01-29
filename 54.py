import sys
from collections import Counter
import pprint

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'poker.txt'

def card_value(card):
  """ Convert textual car representation to numeric value + suit. Numeric values are easier to compare"""
  value, suit = card[0], card[1]
  cv = -1
  if   value == 'T': cv = 10
  elif value == 'J': cv = 11
  elif value == 'Q': cv = 12
  elif value == 'K': cv = 13
  elif value == 'A': cv = 14
  elif value == '1': cv = 14
  else             : cv = int(value)
  return (cv, suit)

assert card_value('AH') == (14,'H')
assert card_value('2D') == (2 ,'D')

def hand_value(cards):
  """ Calculate the value of a hand of 5 cards. Returns a tuple of values, to include all the tie-breaker criteria"""
  c0,c1,c2,c3,c4 = cards
  v0,s0 = card_value(c0) # value and suit
  v1,s1 = card_value(c1)
  v2,s2 = card_value(c2)
  v3,s3 = card_value(c3)
  v4,s4 = card_value(c4)

  vs = sorted([v0,v1,v2,v3,v4]) # to reduce the number of comparison cases
  is_pair1         = vs[0] == vs[1]
  is_pair2         = vs[1] == vs[2]
  is_pair3         = vs[2] == vs[3]
  is_pair4         = vs[3] == vs[4] 
  is_pair          = is_pair1 or is_pair2 or is_pair3 or is_pair4

  is_twoPair1      = vs[0] == vs[1] and vs[2] == vs[3]
  is_twoPair2      = vs[0] == vs[1] and vs[3] == vs[4]
  is_twoPair3      = vs[1] == vs[2] and vs[3] == vs[4] 
  is_twoPair       = is_twoPair1 or is_twoPair2 or is_twoPair3

  is_threeOfAKind  = vs[0] == vs[1] == vs[2] or vs[1] == vs[2] == vs[3] or vs[2] == vs[3] == vs[4]

  is_straight      = vs[0]+4 == vs[1]+3 == vs[2]+2 == vs[3]+1 == vs[4]
  
  is_flush         = s0 == s1 == s2 == s3 == s4
  
  is_fullHouse1    = vs[0] == vs[1] and vs[2] == vs[3] == vs[4]
  is_fullHouse2    = vs[0] == vs[1] == vs[2] and vs[3] == vs[4]
  is_fullHouse     = is_fullHouse1 or is_fullHouse2
  
  is_fourOfAKind   = vs[0] == vs[1] == vs[2] == vs[3] or vs[1] == vs[2] == vs[3] == vs[4] 
  
  is_straightFlush = is_straight and is_flush
  
  is_royalFlush    = is_straightFlush and vs[0] == 10

  # hand_value will have :
  #  number indicating which rank the suit fell in
  #  Values of the card(s) involved in the rank.
  #  Values of all the cards in the hand in descending order.
  # This makes comparing hand-values trivial.

  hand_value = []
  if is_royalFlush:
    hand_value.append(9)
  elif is_straightFlush:
    hand_value.append(8)
  elif is_fourOfAKind:
    hand_value.append(7)
    hand_value.append(vs[2])
  elif is_fullHouse:
    hand_value.append(6)
    hand_value.append(vs[2])  # vs[2] is always part of the triple. Compare triple before double.
    if is_fullHouse1:
      hand_value.append(vs[1])
    if is_fullHouse2:
      hand_value.append(vs[3])
  elif is_flush :
    hand_value.append(5)
  elif is_straight:
    hand_value.append(4)
  elif is_threeOfAKind:
    hand_value.append(3)
    hand_value.append(vs[2])
  elif is_twoPair:
    hand_value.append(2)
    hand_value.extend(reversed(sorted([vs[1], vs[3]])))  # larger pair first.
  elif is_pair:
    hand_value.append(1)
    if is_pair1:
      hand_value.append(vs[1])
    if is_pair2:
      hand_value.append(vs[2])
    if is_pair3:
      hand_value.append(vs[3])
    if is_pair4:
      hand_value.append(vs[4])
  else :
    hand_value.append(0)

  # Add all the card values in descending order.
  hand_value.extend(reversed(vs))
  return hand_value

p1_win_count = 0
with open(fname,'r') as fp :
  poker_lines = fp.readlines()
  for pl in poker_lines:
    pls = pl.strip()
    cards = pls.split(' ')
    assert len(cards) == 10
    hand_value_p1 = hand_value(cards[:5])
    hand_value_p2 = hand_value(cards[5:])
    if hand_value_p1 > hand_value_p2:
      p1_win_count += 1

print p1_win_count
