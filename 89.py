import sys
from collections import Counter
import pprint

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'roman.txt'

roman_char_to_num = {
    'I' : 1    ,
    'V' : 5    ,
    'X' : 10   ,
    'L' : 50   ,
    'C' : 100  ,
    'D' : 500  ,
    'M' : 1000 ,
    }

num_to_roman_char = {
    1    : 'I' ,
    5    : 'V' ,
    10   : 'X' ,
    50   : 'L' ,
    100  : 'C' ,
    500  : 'D' ,
    1000 : 'M' ,
    }

def roman_to_num(r):
  nums = [ roman_char_to_num[c] for c  in r ]
  for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
      nums[i] = - nums[i]
  total = sum(nums)
  return total

assert roman_to_num('MMDCCXLIX') == 2749

def find_and_sub(s, find, sub):
  pos = s.find(find)
  if pos == -1 :
    return s
  else :
    ss = s[:pos] + sub + s[pos+len(find):]
    return ss

def num_to_roman(n):
  num = n
  r = ''
  for i in sorted(num_to_roman_char.keys(), reverse=True):
    while num >= i :
      num -= i
      r += num_to_roman_char[i]
  assert (num==0)
  r = find_and_sub(r, 'DCCCC', 'CM')
  r = find_and_sub(r,  'CCCC', 'CD')
  r = find_and_sub(r, 'LXXXX', 'XC')
  r = find_and_sub(r,  'XXXX', 'XL')
  r = find_and_sub(r, 'VIIII', 'IX')
  r = find_and_sub(r,  'IIII', 'IV')
  return r

assert num_to_roman(2749) == 'MMDCCXLIX'

saving = 0
with open(fname,'r') as fr :
  roman_lines = fr.readlines()
  for rl in roman_lines:
    rls = rl.strip()
    old_len = len(rls)
    new_len = len( num_to_roman( roman_to_num( rls ) ) )
    assert (new_len <= old_len)
    saving += (old_len - new_len)

print saving
