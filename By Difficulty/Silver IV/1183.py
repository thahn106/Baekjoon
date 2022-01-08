N=int(input())
d = []
for i in range(N):
    a,b = map(int,input().split())
    d.append(b-a)
d.sort()
if N % 2:
    print(1)
else:
    i = N//2
    print(d[i]-d[i-1]+1)
