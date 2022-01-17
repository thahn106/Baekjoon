import sys
input = sys.stdin.buffer.readline

N = int(input())
edges = list(map(int,input().split()))
M = int(input())

q = []
graph = [[] for i in range(N)]
for i,e in enumerate(edges):
    if i!=M:
        if e == -1:
            q.append(i)
        elif e != M:
            graph[e].append(i)

ans = 0
while q:
    cur_node = q.pop()
    if graph[cur_node]:
        for nbr in graph[cur_node]:
            q.append(nbr)
    else:
        ans +=1
print(ans)
