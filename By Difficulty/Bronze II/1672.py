def t(c):
    if c=="A":
        return 0
    elif c=="G":
        return 1
    elif c=="C":
        return 2
    elif c=="T":
        return 3

grid = [[0,2,0,1],[2,1,3,0],[0,3,2,1],[1,0,1,3]]

N = int(input())
S = input()
cur = t(S[-1])
for i in range(N-1):
    n = t(S[N-2-i])
    cur = grid[cur][n]

print("AGCT"[cur])
