for i in range(1000,10000):
    a = []
    for j in [10,12,16]:
        d = 0
        t = i
        while t:
            t,r = divmod(t,j)
            d+=r
        a.append(d)
    if max(a)==min(a):
        print(i)
