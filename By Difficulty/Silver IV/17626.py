from math import sqrt,ceil
N = int(input())

def isq(n): return round(sqrt(n)) == sqrt(n)

if isq(N):
    print(1)
else:
    # 2
    found = False
    for i in range(1,ceil(sqrt(N))):
        if isq(N-i*i):
            print(2)
            found = True
            break
    if not found:
        for i in range(1,ceil(sqrt(N))):
            ni = N-i*i
            for j in range(1,ceil(sqrt(ni))):
                if isq(ni-j*j):
                    print(3)
                    found = True
                    break
            if found:
                break
        if not found:
            print(4)
