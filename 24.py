# assumes l is already sorted : easy to do once before the top gen_prem call.
# So, going left to right is equivalent to lex order, and no sorting is needed.
def gen_perm(l):
  ls = l
  ll = len(ls)
  if ll == 1:
    yield l
    return
  for i in xrange(ll): 
    a = l[i]
    b = l[0:i] + l[i+1:ll]
    g = gen_perm(b)
    for p in g:
      yield [a] + p
  return

#N = 5
#digits = range(N)
#dp = gen_perm(digits)
#for p in dp:
#    sp = map (str, p)
#    print "".join(sp)

N = 10
digits = range(N)
dp = gen_perm(digits)
count = 0
for p in dp:
  count += 1
  if (count == 1e6):
    sp = map (str, p)
    print "".join(sp)
    break


# 4.84 secs
