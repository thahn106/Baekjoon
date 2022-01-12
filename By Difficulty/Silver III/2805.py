from math import ceil
N,M = map(int,input().split())
trees = list(map(int,input().split()))
trees.append(0)
trees.sort()

i = N
h = trees[-1]
cutting = 0
while M:
    if trees[i]<h:
        if (h-trees[i])*cutting >= M:
            h -= ceil(M/cutting)
            break
        else:
            M -= (h-trees[i])*cutting
            h  = trees[i]
    i -=1
    cutting +=1
print(h)
