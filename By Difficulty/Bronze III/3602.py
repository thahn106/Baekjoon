b,w = map(int,input().split())
if max(b,w)==0:
    print("Impossible")
else:
    ans = 0
    for i in range(1,200):
        a = (i**2)//2
        f = a
        if i%2:
            f+=1
        if min(b,w)>=a and max(b,w)>=f:
            ans = i
        else:
            break
    print(ans)
