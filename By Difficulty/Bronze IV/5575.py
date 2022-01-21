for i in range(3):
    a,b,c,d,e,f = list(map(int,input().split()))
    time = (d-a)*3600+(e-b)*60+(f-c)
    h,s = divmod(time,3600)
    m,s = divmod(s,60)
    print("{} {} {}".format(h,m,s))
