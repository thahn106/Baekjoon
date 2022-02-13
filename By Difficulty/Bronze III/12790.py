for t in range(int(input())):
    a = list(map(int,input().split()))
    HP = 1*max(1, a[0]+a[4])
    MP = 5*max(1, a[1]+a[5])
    A = 2*max(0, a[2]+a[6])
    D = 2*(a[3]+a[7])
    print(HP+MP+A+D)
