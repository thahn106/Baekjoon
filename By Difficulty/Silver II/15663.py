from itertools import permutations
N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

ans = []
for ss in permutations(nums,M):
    ans.append(tuple(ss))
ans = set(ans)
ans = list(ans)
ans.sort()

for ss in ans:
    print(*ss)
