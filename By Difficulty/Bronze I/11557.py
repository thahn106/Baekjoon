for t in range(int(input())):
    ls = []
    for n in range(int(input())):
        a,b = input().split()
        ls.append((int(b),a))
    ls.sort()
    print(ls[-1][1])
