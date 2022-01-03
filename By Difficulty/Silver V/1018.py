N,M = map(int,input().split())

ans  = 32
dp = []
for i in range(N):
    row = input()
    dr = [0]
    rr = 0
    for j in range(M):
        if ((i+j)%2 and row[j]=="W") or ((i+j)%2==0 and row[j]=="B"):
            rr +=1
        dr.append(rr)
    dp.append(dr)

for i in range(N-7):
    for j in range(M-7):
        temp = 0
        for k in range(8):
            temp += (dp[i+k][j+8]- dp[i+k][j])
        ans = min(ans,min(temp,64-temp))
print(ans)
