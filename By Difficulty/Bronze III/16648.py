t,p = map(int,input().split())

if p<20:
    P = 80 + (20-p)*2
else:
    P = 100-p
print((120-P)/(P/t))
