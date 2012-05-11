tns = []
pns = []
hns = []
i = 1
while True :
  tns.append(i*(i+1)/2)
  pns.append(i*(3*i-1)/2)
  hns.append(i*(2*i-1))
  if tns[-1] in pns and tns[-1] in hns :
    print i, tns[-1]
    if i > 285 :
      break
  i += 1
