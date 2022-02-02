for t in range(int(input())):
    a = list(map(int,input().split()))
    s = []
    for i in a:
        if i%2==0:
            s.append(i)
    print("{} {}".format(sum(s),min(s)))
