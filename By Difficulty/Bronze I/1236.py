N,M = map(int,input().split())
col = [1 for i in range(M)]
row = N
for n in range(N):
    found = False
    s = input()
    for i in range(M):
        if s[i]=='X':
            col[i] = 0
            found = True
    if found:
        row -=1
print(max(sum(col),row))
