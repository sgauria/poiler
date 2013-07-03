def num_is_increasing(n):
  if (n < 10):
    return True
  else :
    ns = str(n)
    for j in range(1,len(ns)):
      i = j-1;
      if int(ns[i]) > int(ns[j]) :
        return False
    return True

def num_is_decreasing(n):
  if (n < 10):
    return True
  else :
    ns = str(n)
    for j in range(1,len(ns)):
      i = j-1;
      if int(ns[i]) < int(ns[j]) :
        return False
    return True

assert (num_is_increasing(134468) == True)
assert (num_is_decreasing(134468) == False)
assert (num_is_increasing(66420 ) == False)
assert (num_is_decreasing(66420 ) == True)

def num_is_bouncy (n):
  if (n < 100) :
    return False 
  else :
    inc = num_is_increasing(n)
    dec = num_is_decreasing(n)
    if not inc and not dec :
      return True 
    else :
      return False

assert (num_is_bouncy(134468) == False)
assert (num_is_bouncy(66420 ) == False)
assert (num_is_bouncy(155349) == True )

bouncy_count = 0
n = 1
while True :
  if num_is_bouncy(n) :
    bouncy_count += 1
  if (1.0 * bouncy_count / n) >= 0.99 :
    print n, bouncy_count, (1.0 * bouncy_count / n)
    break
  if (n % 10000 == 0) :
    print n, bouncy_count, (1.0 * bouncy_count / n)
  n += 1


