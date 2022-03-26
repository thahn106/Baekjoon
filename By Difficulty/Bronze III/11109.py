for t in range(int(input())):
    d,n,s,p = map(int,input().split())
    par = d+n*p
    ser = n*s
    if ser< par:
        print("do not parallelize")
    elif par<ser:
        print("parallelize")
    else:
        print("does not matter")
