import sys

if len (sys.argv) >= 2:
  fname = sys.argv[1]
else :
  fname = 'matrix.txt'

fm = open(fname,'r')
mlines = fm.readlines()
matrix = [map(int,l.split(',')) for l in mlines]
fm.close()
#print matrix[2][3]

mht = len(matrix)
mwd = len(matrix[0])

min_path_sums = [ row[:] for row in matrix ]

for y in range(mht-1,-1,-1) :
  for x in range(mwd-1,-1,-1) :
    candidate = -1
    if (y < mht-1):
      if (min_path_sums[y+1][x] < candidate or candidate == -1):
	candidate = min_path_sums[y+1][x]
    if (x < mwd-1):
      if (min_path_sums[y][x+1] < candidate or candidate == -1):
	candidate = min_path_sums[y][x+1]
    if (candidate > -1):
      min_path_sums[y][x] += candidate

print min_path_sums[0][0]
