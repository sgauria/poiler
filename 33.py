# b -> big
# s -> small
# nr -> numerator
# dr -> denominator
# 0,1 -> digit0, digit1

cool_nrs = []
cool_drs = []

for bnr in xrange(10,100): 
  for bdr in xrange(bnr+1,100): 
    bnr0 = bnr % 10
    bnr1 = int(bnr/10)
    bdr0 = bdr % 10
    bdr1 = int(bdr/10)
    snr,sdr = 1,1
    removed = 0
    if (bnr0 == bdr0):
      snr,sdr = bnr1,bdr1
      removed = bnr0
    if (bnr1 == bdr0):
      snr,sdr = bnr0,bdr1
      removed = bnr1
    if (bnr0 == bdr1):
      snr,sdr = bnr1,bdr0
      removed = bnr0
    if (bnr1 == bdr1):
      snr,sdr = bnr0,bdr0
      removed = bnr1
    if (sdr != 0 and removed != 0):
      if ((1.0 * bnr / bdr) == (1.0 * snr / sdr)):
	print bnr,"/",bdr," :: ",snr,"/",sdr
	cool_nrs.append(snr)
	cool_drs.append(sdr)

# This calculation is not perfect, but it'll do for this problem.
prod = 1
for i in cool_drs:
  prod *= i
for j in cool_nrs:
  if prod % j == 0:
    prod /= j

print prod
  
