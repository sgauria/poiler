def fact(n) :
  if n <= 1:
    return 1
  return n * fact(n-1)

#calculate the nth permutation of l
def get_perm (l,n):
  #print l, n
  ll = len(l)
  if ll == 1 :
    return l
  f = fact(ll-1)
  i = int(n / f)
  j = int(n % f)
  p = [l[i]] + get_perm(l[0:i] + l[i+1:ll], j)
  return p

gp = get_perm (range(10), (1000000 - 1))
print "".join (map (str, gp))

# 0.05 secs
