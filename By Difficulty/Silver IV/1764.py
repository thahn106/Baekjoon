import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left
N,M = map(int,input().split())

nlist = ["" for i in range(N)]
for n in range(N):
    nlist[n] = str(input().strip(),'utf-8')
mlist = ["" for i in range(M)]
for m in range(M):
    mlist[m] = str(input().strip(),'utf-8')
nlist.sort()
mlist.sort()
n = 0
m = 0
ans = []
while n<N and m<M:
    ns = nlist[n]
    ms = mlist[m]
    if ns == ms:
        ans.append(ns)
        n+=1
        m+=1
    elif ns<ms:
        n+=1
    else:
        m+=1
ans.sort()

sys.stdout.write(str(len(ans))+"\n")
for s in ans:
    sys.stdout.write(s+"\n")
sys.stdout.flush()
