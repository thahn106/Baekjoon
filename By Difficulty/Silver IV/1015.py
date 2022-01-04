N = int(input())
a = list(map(int,input().split()))
b = list(zip(a, range(N)))
b.sort()
c = [0 for i in range(N)]
for i in range(N):
    c[b[i][1]]=i
print(*c)
