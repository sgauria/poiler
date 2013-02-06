import sys
from collections import Counter
import pprint
import itertools

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'cipher1.txt'

NCP = 3 # characters in passkey

def possible_keys():
  for i in range(ord('a'), ord('z')):
    for j in range(ord('a'), ord('z')):
      for k in range(ord('a'), ord('z')):
	key = [i,j,k]
	yield key

with open(fname,'r') as fp :
  mlines = fp.readlines()
  crypted = mlines[0].split(',')
  crypted = map(int, crypted)
  for pkey in possible_keys():
    decrypted = []
    ptr = 0
    for c in crypted:
      d = c ^ pkey[ptr]
      ptr = (ptr + 1) % NCP
      if not (0x20 <= d <= 0x7E) : 
	break # not printable.
      decrypted.append(d)
    else :
      key_str = "".join(map(chr, pkey))
      dec_str = "".join(map(chr, decrypted))
      if " the " in dec_str: # Not too rigorous, but it works.
	print key_str, "\n"
	print dec_str, "\n"
	print sum(decrypted)
	break
