a = list(map(int,input().split()))
a.sort()
if a[2]==a[0]:
    print(10000+max(a)*1000)
elif (a[0]==a[1])or (a[2]==a[1]):
    print(1000+100*a[1])
else:
    print(100*a[2])
