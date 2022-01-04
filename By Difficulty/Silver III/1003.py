fib = [1,0]
for i in range(41):
    fib.append(fib[-1]+fib[-2])

for t in range(int(input())):
    N = int(input())
    print("{} {}".format(fib[N],fib[N+1]))
