import sys

for t in range(int(input())):
    n = int(sys.stdin.readline())
    ans = n
    while n>1:
        if n%2: n = 3*n+1
        else: n = n//2
        ans = max(n,ans)
    sys.stdout.write(str(ans)+'\n')
sys.stdout.flush()
