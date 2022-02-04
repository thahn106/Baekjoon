a,d,x = map(int,input().split())
while a or d or x:
    if (x-a)//d >= 0 and (x-a)/d == (x-a)//d:
        print((x-a)//d+1)
    else:
        print("X")
    a,d,x = map(int,input().split())
