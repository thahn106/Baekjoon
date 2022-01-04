N,M = map(int,input().split())
packs = []
singles = []
for m in range(M):
    a,b = map(int,input().split())
    packs.append(a)
    singles.append(b)

p = min(packs)
s = min(singles)
q,r = divmod(N,6)
print(q*min(p, 6*s)+min(p, r*s))
