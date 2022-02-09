t = 1
O,W = map(int,input().split())
dead = False
while O or W:
    a, N = input().split()
    if a == "E":
        W -= int(N)
        if W <=0:
            dead = True
    elif a == "F":
        W += int(N)
    else:
        if dead:
            print("{} RIP".format(t))
        elif O/2 < W < 2*O:
            print("{} :-)".format(t))
        else:
            print("{} :-(".format(t))
        t += 1
        dead = False
        O,W = map(int,input().split())
