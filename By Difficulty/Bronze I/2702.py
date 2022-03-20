from math import gcd, lcm
for t in range(int(input())):
    a,b = map(int,input().split())
    print(lcm(a,b), gcd(a,b))
