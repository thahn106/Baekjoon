for t in range(int(input())):
    k = list(map(int,input().split()))
    e = 0
    o = 0
    for i in k[1:]:
        if i%2:
            o+=i
        else:
            e+=i
    if e>o:
        print("EVEN")
    elif o>e:
        print("ODD")
    else:
        print("TIE")
