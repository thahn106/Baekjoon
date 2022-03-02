from math import sqrt

t = 0
a,b,c = map(int,input().split())
while a and b and c:
    if a == -1:
        a = c*c-b*b
        if a>0:
            a = sqrt(a)
            ans = f"a = {a:.3f}"
        else:
            ans = "Impossible."
    elif b == -1:
        b = c*c-a*a
        if b>0:
            b = sqrt(b)
            ans = f"b = {b:.3f}"
        else:
            ans = "Impossible."
    else:
        c  = sqrt(a*a+b*b)
        ans = f"c = {c:.3f}"
    if t:
        print("")
    print(f"Triangle #{t+1}")
    print(ans)
    t+=1
    a,b,c = map(int,input().split())
