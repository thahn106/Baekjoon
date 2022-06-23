import sys

M = 1000001
ref = [1]*M
for i in range(2, M):
    for j in range(i, M, i):
        ref[j] += i

ans = [0]*M
for i in range(1, M):
    ans[i] = ans[i-1]+ref[i]

N = int(sys.stdin.readline())
for n in range(N):
    t = int(sys.stdin.readline())
    sys.stdout.write(str(ans[t])+'\n')
sys.stdout.flush()
