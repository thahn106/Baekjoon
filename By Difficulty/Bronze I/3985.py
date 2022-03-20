N = int(input())
cake = [0]*N
exA = 0
exN = 0
acA = 0
acN = 0
for L in range(int(input())):
    l,r = map(int,input().split())
    ex = r-l+1
    if ex>exA:
        exA = ex
        exN = L+1
    ac = 0
    for i in range(l-1,r):
        if not cake[i]:
            cake[i]=L+1
            ac +=1
    if ac>acA:
        acA = ac
        acN = L+1

print(exN)
print(acN)
