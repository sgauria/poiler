def digitial_sum(n):
  sum = 0
  for d in str(n):
    sum += int(d)
  return sum

N=100
maxds = maxa = maxb = 0

for a in range(1,N+1):
  for b in range(1,N+1):
    ds = digitial_sum(a**b)
    if (ds > maxds) :
      maxds = ds
      maxa = a
      maxb = b

print maxds, maxa, maxb, (maxa**maxb)

