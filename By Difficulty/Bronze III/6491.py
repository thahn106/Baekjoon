end = False
while True:
    a = list(map(int,input().split()))
    for n in a:
        if n == 0:
            end = True
            break
        ans = 0
        for i in range(1,n):
            if n%i==0:
                ans += i
            if ans>n:
                break
        if ans<n:
            c = "DEFICIENT"
        elif ans == n:
            c = "PERFECT"
        else:
            c = "ABUNDANT"
        print(n,c)
    if end:
        break
