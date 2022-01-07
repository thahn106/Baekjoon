N,M = map(int,input().split())
a = list(map(int,input().split()))
know = [False for i in range(N+1)]
check = []
for p in a[1:]:
    know[p] = True
    check.append(p)
parties = [list(map(int,input().split()))[1:] for m in range(M)]
tp = [False for m in range(M)]
while check:
    p = check.pop()
    for m in range(M):
        if not tp[m] and p in parties[m]:
            tp[m] = True
            for pi in parties[m]:
                if not know[pi]:
                    know[pi]=True
                    check.append(pi)
print(M-sum(tp))
