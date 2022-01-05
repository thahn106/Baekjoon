for t in range(int(input())):
    n,m,K = map(int,input().split())
    board = [[0 for j in range(m)] for i in range(n)]
    unvisited = []
    for k in range(K):
        x,y = map(int,input().split())
        board[x][y] = 1
        unvisited.append((x,y))
    def dfs(a,b):
        to_visit = [(a,b)]
        while to_visit:
            i,j = to_visit.pop()
            if board[i][j] == 1:
                board[i][j]=0
                if i>0:
                    to_visit.append((i-1,j))
                if i<n-1:
                    to_visit.append((i+1,j))
                if j>0:
                    to_visit.append((i,j-1))
                if j<m-1:
                    to_visit.append((i,j+1))
    ans = 0
    for cell in unvisited:
        a,b = cell
        if board[a][b]==1:
            ans+=1
            dfs(a,b)
    print(ans)
