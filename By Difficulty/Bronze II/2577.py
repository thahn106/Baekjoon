N = 1
for i in range(3):
    N*=int(input())
ans = [0 for i in range(10)]
for c in str(N):
    ans[int(c)]+=1
for i in range(10):
    print(ans[i])
