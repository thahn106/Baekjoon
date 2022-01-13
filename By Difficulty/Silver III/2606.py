N = int(input())
E = int(input())

visited = [0 for i in range(N)]
graph = [ [] for i in range(N)]
for e in range(E):
    u,v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

q = [0]
while q:
    cur = q.pop()
    visited[cur] = 1
    for n in graph[cur]:
        if not visited[n]:
            q.append(n)

print(sum(visited)-1)
