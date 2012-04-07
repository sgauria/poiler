d = [1]

step = 2
for i in xrange(500):
  for j in xrange(4):
    d.append(d[4*i+j] + step)
  step += 2

print d
print sum(d)

