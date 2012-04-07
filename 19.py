def day_of_months():
  year = 1901
  while (True):
    yield 31 # Jan
    if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
      yield 29
    else:
      yield 28
    yield 31 # Mar
    yield 30 # Apr
    yield 31 # May
    yield 30 # Jun
    yield 31 # Jul
    yield 31 # Aug
    yield 30 # Sep
    yield 31 # Oct
    yield 30 # Nov
    if (year == 2000):
      break
    yield 31 # Dec
    year += 1

dom = day_of_months()

# sunday = 0 ... saturday = 6
day = 2 # Jan 1 1901 is a Tuesday

count = 0
for x in dom :
  if (day == 0):
    count += 1
  day = (day + x) % 7

print count
