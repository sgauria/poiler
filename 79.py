import sys
from collections import Counter
import pprint

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'keylog.txt'

# Collect left right statistics.
char_stats = {}
with open(fname,'r') as fkl :
  keylog_lines  = fkl.readlines()
  for kll in keylog_lines:
    kllc = kll.strip()
    for pos,c in enumerate(kllc) :
      if c not in char_stats:
	char_stats[c] = {}
	char_stats[c]['left']  = Counter()
	char_stats[c]['right'] = Counter()
      char_stats[c]['left'].update(kllc[:pos])
      char_stats[c]['right'].update(kllc[pos+1:])

# Reduce stats to number of left right chars. 
# NOTE !! : Assuming all unique characters here.
char_stats2 = {}
for c in char_stats:
  char_stats2[c] = {}
  char_stats2[c]['left']  = len(char_stats[c]['left'].most_common() )
  char_stats2[c]['right'] = len(char_stats[c]['right'].most_common())

# pprint.pprint(char_stats2)

# Convert dict to list of tuples 
cs3 = []
for c in char_stats2:
  t = (c, char_stats2[c]['left'])
  cs3.append( t )

# sort by number of left side characters ( 0 ... )
cs3.sort(key=lambda tup:tup[1])

# Result is just joining the characters back together.
result = "".join( x[0] for x in cs3 )

print result
