from math import gcd
A,B = map(int,input().split())
A,B = B-A,B
print("{} {}".format(A//gcd(A,B),B//gcd(A,B)))
