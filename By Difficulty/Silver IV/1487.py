N = int(input())

P = []
D = []
for i in range(N):
    p,d = map(int,input().split())
    P.append(p)
    D.append(d)

profit = 0
ans = 0
for price in sorted(list(P)):
    tp = 0
    for i in range(N):
        if price<=P[i] and price>D[i]:
            tp += price-D[i]
    if tp > profit:
        profit = tp
        ans = price
print(ans)
