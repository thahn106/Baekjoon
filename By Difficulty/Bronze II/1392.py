from bisect import bisect_right
N,Q = map(int,input().split())
r = 0
q = [0]
for n in range(N):
    r+= int(input())
    q.append(r)
for s in range(Q):
    a = bisect_right(q,int(input()))
    print(a)
