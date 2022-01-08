N = int(input())

ans = 0
for i in range(1,N+1):
    if i<100:
        ans +=1
    else:
        check = True
        a = [int(d) for d in list(str(i))]
        d = a[1]-a[0]
        for j in range(1,len(a)):
            if  d != (a[j]-a[j-1]):
                check= False
        if check:
            ans +=1
print(ans)
