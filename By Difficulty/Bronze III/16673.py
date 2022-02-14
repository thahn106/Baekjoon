C,K,P = map(int,input().split())
ans = 0
for i in range(C+1):
    ans += K*i+P*i*i
print(ans)
