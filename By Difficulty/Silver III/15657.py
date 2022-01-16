from itertools import combinations_with_replacement
N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

for ss in combinations_with_replacement(nums,M):
    print(*ss)
