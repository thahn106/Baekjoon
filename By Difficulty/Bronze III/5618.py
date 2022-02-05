import sys
from math import gcd

n = int(input())
a = list(map(int,input().split()))
g = a[0]
for i in a[1:]:
    g= gcd(g,i)
for i in range(1,g+1):
    if not g%i:
        sys.stdout.write("{}\n".format(i))
sys.stdout.flush()
