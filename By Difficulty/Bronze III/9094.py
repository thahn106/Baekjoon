for t in range(int(input())):
    n,m = map(int,input().split())
    ans = 0
    for a in range(1,n-1):
        for b in range(a+1,n):
            if (a*a+b*b+m)%(a*b)==0:
                ans +=1
    print(ans)
