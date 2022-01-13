N = int(input())

ans = [-1 for i in range(N+1)]

ans[1] = 0
for i in range(2,N+1):
    cand = [ans[i-1]]
    if i%2 == 0:
        cand.append(ans[i//2])
    if i%3 ==0:
        cand.append(ans[i//3])
    ans[i] = min(cand)+1
print(ans[N])
