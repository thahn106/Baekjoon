from itertools import combinations
k,n = map(int,input().split())
a = sorted(input().split())

for elems in combinations(a,k):
    vowels = 0
    for i in elems:
        if i in "aeiou":
            vowels+=1
    if vowels>=1 and k-vowels>=2:
        print("".join(elems))
