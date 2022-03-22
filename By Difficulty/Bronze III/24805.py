from math import ceil
a,b,h = map(int,input().split())
if a>=h:
    print(1)
else:
    print(ceil((h-b)/(a-b)))
