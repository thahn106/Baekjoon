for t in range(int(input())):
    c = []
    for i in range(4):
        x,y = map(int,input().split())
        c.append((x,y))
    d = []
    for c1 in range(3):
        p1 = c[c1]
        for c2 in range(c1+1,4):
            p2 = c[c2]
            d.append((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    d.sort()
    print(int(d[0]==d[1]==d[2]==d[3] and d[4]==d[5] and d[3]!=d[4]))
