import sys
input = sys.stdin.buffer.readline

N = int(input())
graph = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

vst = [False for i in range(N)]

parents = [0 for i in range(N)]

order = []
q = [0]
while q:
    cur_node = q.pop()
    order.append(cur_node)
    vst[cur_node] = True
    for nbr in graph[cur_node]:
        if not vst[nbr]:
            parents[nbr]=cur_node
            q.append(nbr)

for node in parents[1:]:
    print(node+1)
