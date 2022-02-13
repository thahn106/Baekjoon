for t in range(int(input())):
    c,v = map(int,input().split())
    d,r = divmod(c,v)
    print("You get {} piece(s) and your dad gets {} piece(s).".format(d,r))
