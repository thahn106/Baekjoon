from math import lcm

a = list(map(int,input().split()))
ans = 10000000000
for i in range(0,3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans = min(lcm(a[i],a[j],a[k]),ans)
print(ans)
