for t in range(int(input())):
    N,K = map(int, input().split())
    D = list(map(int,input().split()))
    graph = [[] for i in range(N)]
    incoming = [0 for i in range(N)]
    for k in range(K):
        X,Y = map(int,input().split())
        graph[X-1].append(Y-1)
        incoming[Y-1] +=1

    # Topological Sort
    order = []
    S = []
    for i in range(N):
        if not incoming[i]:
            S.append(i)

    while S:
        x = S.pop()
        order.append(x)
        for y in graph[x]:
            incoming[y]-=1
            if incoming[y]==0:
                S.append(y)

    endtime = [0 for i in range(N)]
    for x in order:
        endtime[x]+=D[x]
        for y in graph[x]:
            endtime[y] = max(endtime[y],endtime[x])
    W = int(input())
    print(endtime[W-1])
