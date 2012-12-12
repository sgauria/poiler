from poiler_common import is_prime
import itertools

digit_can = [0,1,2,3,4,5,6,7,8,9,'X']
odd_can   = [1,3,7,9]

def candidate_generator():
  """ Generates all possible valid patterns that we need to test"""
  num_digits = 2
  while True:
    for c in itertools.combinations_with_replacement(digit_can, num_digits):
      for pc in itertools.permutations(c):
	if (pc[-1] in odd_can) and ('X' in pc) and (pc[0] != 0):
	  yield pc
    num_digits += 1


def digit_list_to_num(l):
  """ Convert a list or tuple to a number. [1,2,3] -> 123"""
  n = reduce (lambda x,y : 10*x+y, l)
  return n


def one_list_to_n_numbers(l): # 9 or 10 
  """Starting with the pattern list, yield all the valid numbers that it generates"""
  start = 1 if (l[0] == 'X') else 0
  for i in range(start, 10):
    mod_l = [i if (j == 'X') else j for j in l]
    num = digit_list_to_num(mod_l)
    yield num
    

max_num_prime = 0
for pattern in candidate_generator():
  actual_primes = []
  not_prime = 0
  num_prime = 0
  for possible_prime in one_list_to_n_numbers(pattern):
    if is_prime(possible_prime):
      num_prime += 1
      actual_primes.append(possible_prime)
    else :
      not_prime += 1
    if not_prime >= 10-max_num_prime:
      break
  if num_prime > max_num_prime:
    max_num_prime = num_prime
    print pattern, actual_primes, num_prime
    if num_prime >= 8:
      print "===="
      print actual_primes[0]
      break


