import sys
N = int(input())
li = [int(sys.stdin.readline()) for i in range(N)]
cur = 0
ans = 0
for i in li[::-1]:
    if i>cur:
        cur = i
        ans +=1
print(ans)
