from math import ceil
N, K = map(int, input().split())

count = [0]*12
for n in range(N):
    S, Y = map(int, input().split())
    count[S*6+Y-1] += 1

ans = 0
for c in count:
    ans += ceil(c/K)

print(ans)
