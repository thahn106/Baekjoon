from itertools import combinations_with_replacement
N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

ans = []
for ss in combinations_with_replacement(nums,M):
    ans.append(tuple(ss))
ans = set(ans)
ans = list(ans)
ans.sort()

for ss in ans:
    print(*ss)
