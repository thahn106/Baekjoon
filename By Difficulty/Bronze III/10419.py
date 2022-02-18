from math import floor, sqrt
for t in range(int(input())):
    d = int(input())
    ans = 0
    for i in range(101):
        if i+i*i<=d:
            ans = i
        else:
            break
    print(ans)
