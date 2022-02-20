from math import ceil
N = int(input())
A = list(map(int,input().split()))
b,c = map(int,input().split())
ans = N
for i in A:
    ans += ceil(max(0,i-b)/c)
print(ans)
