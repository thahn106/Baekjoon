from itertools import combinations
x = list(map(int,input().split()))
ans = 0
for ss in combinations(x, 2):
    if sum(ss):
        ans+=1

for ss in combinations(x, 3):
    if sum(ss):
        ans+=1
print(ans%2)
