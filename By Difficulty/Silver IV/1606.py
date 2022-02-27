x,y = map(int,input().split())

d = max(abs(x+y),abs(x),abs(y))
n = 3*d*(d+1) +1
if x == d:
    print(n+y)
elif -x == d:
    print(n-3*d-y)
elif y == d:
    print(n-5*d-x)
elif -y == d:
    print(n-2*d+x)
elif x>0:
    print(n-5*d-x)
else:
    print(n-3*d-y)
