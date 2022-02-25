A = 125*250
x,y = map(int,input().split())
if not x or not y:
    if x:
        if x<=125:
            b = (A)/(250-x)
            a = 250-b
        else:
            b = A/x
            a = 0
    else:
        if y<=125:
            a = (A)/(250-y)
            b = 250-a
        else:
            a = A/y
            b = 0
else:
    if y>125:
        a = 250-A/y
        b = 0
    else:
        b = 250-A/x
        a = 0

print(f"{a:.2f} {b:.2f}")
