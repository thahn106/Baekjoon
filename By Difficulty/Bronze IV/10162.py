T = int(input())

A,T = divmod(T,300)
B,T = divmod(T,60)
C,T = divmod(T,10)
if T:
    print(-1)
else:
    print("{} {} {}".format(A,B,C))
