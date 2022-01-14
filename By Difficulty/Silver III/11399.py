N = int(input())
P = list(map(int,input().split()))
P.sort()
ans = 0
run = 0
for i in P:
    run += i
    ans +=run
print(ans)
