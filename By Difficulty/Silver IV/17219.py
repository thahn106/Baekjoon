import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left
N,M = map(int,input().split())

web = [0 for i in range(N)]
for n in range(N):
    a,b = [str(i, 'utf-8') for i in input().strip().split()]
    web[n] = (a,b)
sd =  sorted(web)
for m in range(M):
    q = str(input().strip(),'utf-8')
    sys.stdout.write(str(sd[bisect_left(sd, (q,""))][1])+"\n")
sys.stdout.flush()
