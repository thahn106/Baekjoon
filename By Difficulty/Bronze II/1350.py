from math import ceil
N = int(input())
a = list(map(int,input().split()))
C = int(input())

ans = 0
for i in a:
    ans += C*ceil(i/C)
print(ans)
