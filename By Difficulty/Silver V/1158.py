N,K = map(int,input().split())

num = [n+1 for n in range(N)]
ans = []
k=-1
for i in range(N):
    k= (k+K)%len(num)
    ans.append(str(num[k]))
    num.remove(num[k])
    k-= 1
print("<"+", ".join(ans)+">")
