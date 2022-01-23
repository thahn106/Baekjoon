fib = [0,1]
N=int(input())
for n in range(N):
    fib.append(fib[-1]+fib[-2])
print(fib[N])
