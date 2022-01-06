N,M = map(int,input().split())
p = []
for i in range(M):
    p.append(int(input()))

p.sort()
price = 0
ans = 0
for i in range(M):
    if ans < p[i]*(min(N,(M-i))):
        price = p[i]
        ans = p[i]*(min(N,(M-i)))
print("{} {}".format(price, ans))
