ans = []
for t in range(int(input())):
    a = list(map(int,input().split()))
    a.sort()
    if a[0]==a[3]:
        ans.append(a[0]*5000+50000)
    elif a[1]==a[3] or a[0]==a[2]:
        ans.append(a[1]*1000+10000)
    elif a[0]==a[1] and a[2]==a[3]:
        ans.append((a[1]+a[2])*500+2000)
    elif a[0]==a[1]:
        ans.append(a[1]*100+1000)
    elif a[1]==a[2]:
        ans.append(a[2]*100+1000)
    elif a[2]==a[3]:
        ans.append(a[3]*100+1000)
    else:
        ans.append(a[3]*100)

print(max(ans))
