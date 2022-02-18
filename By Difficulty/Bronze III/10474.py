a,b = map(int,input().split())
while a and b:
    d,r = divmod(a,b)
    print("{} {} / {}".format(d,r,b))
    a,b = map(int,input().split())
