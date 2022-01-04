N,M = map(int,input().split())

a = list(map(int, input().split()))
visited = [False for i in range(N)]

def find_next(start, end):
    #Forwards
    f = 0
    c = start
    while not c==end:
        if not visited[c]:
            f+=1
        c +=1
        if c>=N:
            c = 0
    b = 0
    c = start
    while not c == end:
        if not visited[c]:
            b+=1
        c -=1
        if c<0:
            c = N-1
    visited[end]=True
    return min(f,b)


ans = 0
cur = 0
for m in range(M):
    ans += find_next(cur, a[m]-1)
    cur = a[m]-1
    while (m!= N-1) and visited[cur]:
        cur+=1
        if cur>=N:
            cur = 0
print(ans)
