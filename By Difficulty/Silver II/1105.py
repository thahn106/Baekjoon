from math import log, floor
L,R = map(int,input().split())
if floor(log(L,10))<floor(log(R,10)):
    print(0)
else:
    L= str(L)
    R= str(R)
    working = True
    ans = 0
    for i in range(len(L)):
        if L[i]!=R[i]:
            working=False
        elif working:
            if L[i]=="8":
                ans+=1
    print(ans)
