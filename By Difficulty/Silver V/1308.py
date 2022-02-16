def leap(n):
    return n%4==0 and (n%400==0 or not(n%100==0))

months = [31,28,31,30,31,30,31,31,30,31,30,31]

y,m,d=map(int,input().split())
Y,M,D=map(int,input().split())
if (Y-y)>1000 or (Y-y==1000 and (M>m or (M==m and D>=d))):
    print("gg")
else:
    ans = 0
    if Y>y:
        while m<13:
            ans += months[m-1]-(d-1)
            if m==2 and leap(y):
                ans+=1
            m += 1
            d = 1
        y += 1
        m = 1
        d = 1
        while Y>y:
            if leap(y):
                ans +=366
            else:
                ans +=365
            y+=1
    while m<M:
        ans += months[m-1]-(d-1)
        if m == 2 and leap(y):
            ans +=1
        m+=1
        d=1
    if d<D:
        ans += D-d
        d = D
    print("D-{}".format(ans))
