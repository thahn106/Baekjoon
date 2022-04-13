from math import gcd
a, b = map(int, input().split())
m = gcd(a, b)
print('1'*m)
