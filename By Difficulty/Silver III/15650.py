from itertools import combinations
N,M = map(int,input().split())

nums = [i+1 for i in range(N)]

for ss in combinations(nums,M):
    print(*ss)
