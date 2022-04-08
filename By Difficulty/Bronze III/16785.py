from math import ceil
A,B,C = map(int,input().split())
q,r = divmod(C,7*A+B)
print(q*7+ min(7,ceil(r/A)))
