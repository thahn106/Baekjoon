ans = []
for n in range(int(input())):
    a = sorted(list(map(int,input().split())))
    if a[0]==a[2]:
        ans.append(a[2]*1000+10000)
    elif a[0]==a[1] or a[1]==a[2]:
        ans.append(a[1]*100+1000)
    else:
        ans.append(a[2]*100)
print(max(ans))
