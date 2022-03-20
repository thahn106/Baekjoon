for t in range(int(input())):
    a = []
    for p in range(int(input())):
        c,d = input().split()
        a.append((int(c),d))
    a.sort()
    print(a[-1][1])
