import sys
import re
from collections import defaultdict

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'words.txt'

##
## 1> Get the full list of words.
##
fw = open(fname,'r')
wlines = fw.readlines()
words = []
for l in wlines:
  for w in l.split(','):
    words.append( re.sub('"','',w) )
fw.close()
#print words

##
## 2> Find all the anagram pairs.
##
anagram_pairs = []
for i in xrange(len(words)):
  wi = words[i]
  swi = sorted(wi)
  lwi = len(wi)
  for j in xrange(i+1,len(words)):
    wj = words[j]
    if lwi == len(wj):
      if swi == sorted(wj):
	anagram_pairs.append( (wi, wj) )
	#print i, j, wi, wj
#print anagram_pairs, len(anagram_pairs)

##
## 3> Find the longest word in our list
##
max_word_len = max([len(ap[0]) for ap in anagram_pairs])
#print max_word_len

##
## 4> Calculate all the squares upto that length. (Candidate squares for all our words)
##
squares = defaultdict(list)
i = 0
while True :
  i += 1
  sqi = i*i
  lsqi =  len(str(sqi)) 
  if lsqi > max_word_len:
    break
  squares[lsqi].append(str(sqi))
#print squares

##
## 2 functions to simplify the later step
##  Note that num* are actually strings to simplify the digit extraction
##
def is_valid_digit_substitution(word, num):
  d = dict()
  for i in range(len(word)):
    ci = word[i]
    di = num[i]
    if di in d and d[di] != ci:
      return False
    else :
      d[di] = ci
  return True

def digital_translation(word1, num1, word2):
  d = dict(zip(word1, num1))
  num2 = ''
  for c in word2:
    num2 += d[c]
  return num2

##
## 5> for each possible square as a candidate for ap1 : check if the corresponding number for ap2 is also a square
##
ap_squares = []
for ap in anagram_pairs:
  ap1, ap2 = ap
  lap = len(ap1)
  for sq1 in squares[lap]:
    if is_valid_digit_substitution(ap1, sq1):
      sq2 = digital_translation(ap1,sq1,ap2)
      if sq2 in squares[lap]:
	print "%s\t%s\t%s\t%s"%(ap1,sq1,ap2,sq2)
	ap_squares.append(sq1)
	ap_squares.append(sq2)

print "======"
print max(map(int, ap_squares))

# Notes based on reading the threads :
# My code is a bit slow because I precalculate a lot of stuff and store it in
# lists. This way I am possibly doing some more calculations than strictly
# necessary. Putting it all in nested loops might be a little bit faster. Not
# that 1.2 seconds runtime actually is perceptibly slow.
