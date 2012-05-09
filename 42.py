import sys
import re

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'words.txt'

fw = open(fname,'r')
wlines = fw.readlines()
words = []
for l in wlines:
  for w in l.split(','):
    words.append( re.sub('"','',w) )
fw.close()
#print words

# 100 triange numbers should be enough for words up to 190 chars in length.
tns = []
for i in xrange(100):
  tn = i*(i+1)/2
  tns.append(tn)

def cscore(c):
  if ('a' <= c <= 'z'):
    return (ord(c) - ord('a') + 1)
  if ('A' <= c <= 'Z'):
    return (ord(c) - ord('A') + 1)

tcount = 0
for w in words:
  wscore = 0
  for c in w:
    wscore += cscore(c)
  if wscore in tns:
    tcount += 1

print tcount
