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
  for key in itertools.product(range(ord('a'), ord('z')+1), repeat=NCP):
    yield key

with open(fname,'r') as fp :
  crypted = eval(fp.read())
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
