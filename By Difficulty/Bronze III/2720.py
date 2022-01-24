for t in range(int(input())):
    C = int(input())
    Q,r = divmod(C,25)
    D,r = divmod(r,10)
    N,P = divmod(r,5)
    print("{} {} {} {}".format(Q,D,N,P))
