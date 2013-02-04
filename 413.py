def all_substr_nums(num, min_size=1, max_size=float('Inf')):
  mynum = str(num)
  lmn = len(mynum)
  if max_size > lmn:
    max_size = lmn
  for l in range(min_size, max_size+1):
    for start in range(0, lmn-(l-1)):
      yield int(mynum[start:start+l])

assert list(all_substr_nums(5671)) == [5, 6, 7, 1, 56, 67, 71, 567, 671, 5671]

def is_one_child_num_direct(n):
  divisor = len(str(n))
  count = 0
  for nn in all_substr_nums(n):
    if nn % divisor == 0 :
      count += 1
    if count > 1:
      return False
  if count == 1:
    return True
  else :
    return False

is_one_child_num = is_one_child_num_direct

assert is_one_child_num(5671) == True

def F_direct(n):
  """How many numbers below n are one-child numbers."""
  count = 0
  for i in range(1,n):
    if is_one_child_num(i) == True:
      print i
      count += 1
  return count

F = F_direct

assert F(10) == 9
assert F(1000) == 389
#assert F(10000000) == 277674
