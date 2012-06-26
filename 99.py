import math
import sys

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'base_exp.txt'

fbe = open(fname,'r')
base_exp_lines  = fbe.readlines()
base_exp_tuples = []
for lnum,l in enumerate(base_exp_lines, start=1):
  (b,e) = map(int, l.split(','))
  base_exp_tuples.append( ((e*math.log10(b)), b, e, lnum) )
fbe.close()

base_exp_tuples.sort()
mbe = base_exp_tuples[-1]

print "line number =", mbe[3], "base =", mbe[1], "exp =", mbe[2], "log10 of result =", mbe[0]
#print mbe[1], "^", mbe[2], "=", (mbe[1] ** mbe[2])

