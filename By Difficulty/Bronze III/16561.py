from math import comb
n = int(input())
if n%3 or n<9:
    print(0)
else:
    d = (n//3)-3
    print(comb(d+2,2))
