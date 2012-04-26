# Each rectangle in the grid is determined by picking 2 vertical lines and 2 horizontal lines.
# So, the total number of rectangles in a N x M grid is 
#    N+1_C_2  * M+1_C_2
# = (N+1)*N / 2 * (M+1)*M /2
# = N*M*(N+1)*(M+1)/4

target = 2000000
closest = closest_n = closest_m = 0
for n in range(1,1000):
  for m in range(n,1000):
    nr = (n*(n+1)*m*(m+1))/4
    if abs(nr - target) < abs(closest - target): 
      closest = nr
      closest_n = n
      closest_m = m

print closest, closest_n, closest_m, (closest_n*closest_m)
