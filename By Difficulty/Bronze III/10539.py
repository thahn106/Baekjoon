N = int(input())

B = list(map(int,input().split()))
cur = 0
A = []
for i in range(N):
    d = B[i]*(i+1)-cur
    A.append(d)
    cur += d
print(*A)
