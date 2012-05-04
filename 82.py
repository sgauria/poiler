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

inf = float('Inf')
min_path_sums = [ row[:] for row in matrix ]

# Start from right and move left col by col.
#  In each col, find the best path to the next col right, either by moving right directly, or moving up / down within the col and then moving right.
#   Terminate search within each col as soon as possible (when col_sum > the best path found so far)
for x in range(mwd-2,-1,-1) :
  for y in range(mht-1,-1,-1) :
    min_path_sums[y][x] += min_path_sums[y][x+1]
    col_sum = matrix[y][x]
    for y2 in range(y+1,mht):
      col_sum += matrix[y2][x]
      if (col_sum > min_path_sums[y][x]):
        break
      if (col_sum + min_path_sums[y2][x+1] < min_path_sums[y][x]):
	min_path_sums[y][x] = col_sum + min_path_sums[y2][x+1]
    col_sum = matrix[y][x]
    for y2 in range(y-1,-1,-1):
      col_sum += matrix[y2][x]
      if (col_sum > min_path_sums[y][x]):
        break
      if (col_sum + min_path_sums[y2][x+1] < min_path_sums[y][x]):
	min_path_sums[y][x] = col_sum + min_path_sums[y2][x+1]

left_min_paths = [row[0] for row in min_path_sums]
print min(left_min_paths)
