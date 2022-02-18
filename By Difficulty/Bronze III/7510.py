for n in range(int(input())):
    a = list(map(int,input().split()))
    a.sort()
    if n:
        print("")
    print("Scenario #{}:".format(n+1))
    if a[0]**2+a[1]**2==a[2]**2:
        print("yes")
    else:
        print("no")
