from math import gcd
N = int(input())
graph = [[] for i in range(N)]
edges = []

for n in range(N-1):
    a,b,p,q = map(int,input().split())
    graph[a].append((b,n))
    graph[b].append((a,n))
    edges.append((a,b,p,q))

#dfs
visited = [False for i in range(N)]
q = [0]
order = []

while q:
    cur = q.pop()
    if not visited[cur]:
        visited[cur] = True
        for adj,n in graph[cur]:
            if not visited[adj]:
                q.append(adj)
                order.append(n)

r = [0 for i in range(N)]
processed = [False for i in range(N-1)]
for n in order:
    if not processed[n]:
        processed[n] = True
        a,b,p,q = edges[n]
        if r[a]==0 and r[b]== 0:
            r[a]=p
            r[b]=q
        elif r[a]==0:
            for i in range(N):
                r[i] *=q
            r[a] = p*r[b]//q
        elif r[b]==0:
            for i in range(N):
                r[i]*=p
            r[b] = q*r[a]//p
        else:
            print("ERROR")

#cleaning up
d = r[0]
for i in r:
    d = gcd(d,i)

for i in range(N):
    r[i]= r[i]//d
print(*r)
