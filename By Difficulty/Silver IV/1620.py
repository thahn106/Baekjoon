import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

N,M = map(int,input().split())
dex = [0 for i in range(N)]
for n in range(N):
    dex[n]= (str(input().strip(),'utf-8'), n+1)

sd =  sorted(dex)

for m in range(M):
    q = str(input().strip(),'utf-8')
    if ord(q[0])>64:
        sys.stdout.write(str(sd[bisect_left(sd, (q,0))][1])+"\n")
    else:
        sys.stdout.write(dex[int(q)-1][0]+"\n")
    if m%1000==0:
        sys.stdout.flush()
sys.stdout.flush()
