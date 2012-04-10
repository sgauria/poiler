def sum_of_divisors(n):
    sum_div = 0
    for i in range(1,n):
        if (n % i) == 0:
            sum_div += i
    return sum_div

N=10000

sods = [sum_of_divisors(i) for i in range(N)]

sum_of_amis = 0
for i in range(N):
    if sods[i] < N and sods[i] != i:
        if sods[sods[i]] == i:
            sum_of_amis += i
            print (i)

print ("\n===\n",sum_of_amis)
