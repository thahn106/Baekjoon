N,K = map(int,input().split())

possible = True
ans = N

BFS = [set() for k in range(K+1)]
BFS[0].add(N)
for k in range(K):
    if possible:
        flipped = False
        for start in BFS[k]:
            cur = list(str(start))
            for i in range(len(cur)-1):
                for j in range(i+1,len(cur)):
                    if (i == 0 and cur[j]!='0') or i!= 0:
                        flipped = True
                        temp = list(str(start)).copy()
                        temp[i], temp[j] = temp[j], temp[i]
                        BFS[k+1].add(int("".join(temp)))
        if not flipped:
            possible = False
if possible:
    print(max(BFS[K]))
else:
    print(-1)
