t,d = map(int,input().split())
while t or d:
    n = t-d
    if n%2 and n>=3:
        n -= 3
        r = 1
    else:
        r = 0
    print("{} {}".format(n//2, r))
    t,d = map(int,input().split())
