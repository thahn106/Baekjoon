N,M = map(int,input().split())
B = [0]*N
for m in range(M):
    a,b,c = map(int,input().split())
    for x in range(a-1,b):
        B[x]=c

print(*B)
