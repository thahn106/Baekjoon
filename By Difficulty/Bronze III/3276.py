N = int(input())

found = False
n = 2
while not found:
    for r in range(1,n):
        if r*(n-r) >= N:
            print("{} {}".format(r,n-r))
            found = True
            break
    n += 1
