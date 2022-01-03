def op(n):
    a,b = divmod(n,10)
    return b*10+((a+b)%10)

N = int(input())
x = op(N)
cycle = 1
while not x == N:
    x = op(x)
    cycle +=1
print(cycle)
