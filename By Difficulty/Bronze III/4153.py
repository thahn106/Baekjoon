a = list(map(int, input().split()))
a.sort()
while a[2]:
    if a[2]**2==a[1]**2+a[0]**2:
        print("right")
    else:
        print("wrong")
    a = list(map(int,input().split()))
    a.sort()
