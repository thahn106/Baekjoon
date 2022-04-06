x,k = map(int,input().split())
if 7*k<=x:
    print(7000*k)
elif 7*k<=2*x:
    print(3500*k)
elif 7*k<=4*x:
    print(1750*k)
else:
    print(0)
