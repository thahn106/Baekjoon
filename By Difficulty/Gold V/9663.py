N = int(input())

ans = 0
col = [False for i in range(N)]
di = [False for i in range(2*N-1)]
id = [False for i in range(2*N-1)]

def row(r):
    ans = 0
    for c in range(N):
        if not col[c] and not di[r+c] and not id[N-1-c+r]:
            if r == N-1:
                ans += 1
            else:
                col[c], di[r+c], id[N-1-c+r] = True,True,True
                ans += row(r+1)
                col[c], di[r+c], id[N-1-c+r] = False,False,False
    return ans

print(row(0))
