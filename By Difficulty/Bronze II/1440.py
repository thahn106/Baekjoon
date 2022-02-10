from itertools import permutations
time = list(map(int,input().split(":")))
ans = 0

for label in permutations(range(3)):
    working = True
    for j in range(3):
        if label[j]==0:
            if time[j]<1 or time[j]>12:
                working = False
        else:
            if time[j]<0 or time[j]>59:
                working = False
    if working:
        ans+=1
print(ans)
