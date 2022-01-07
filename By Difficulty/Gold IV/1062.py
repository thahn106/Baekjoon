from itertools import combinations

N,K = map(int,input().split())
baseset = ['a','c','i','n','t']
restset = []
for i in range(26):
    s = chr(i+97)
    if s not in baseset:
        restset.append(s)

words = []
for n in range(N):
    s = set()
    for c in input():
        s.add(c)
    words.append(s)
ans = 0
if K>=5:
    for subset in combinations(restset, K-5): #max at 21c10 ~352716
        tempset = set(baseset+list(subset))
        temp = 0
        for s in words: #max 50
            if s.issubset(tempset):
                temp +=1
        ans = max(temp,ans)
print(ans)
