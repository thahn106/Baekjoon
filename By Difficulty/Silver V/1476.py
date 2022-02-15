E,S,M = map(int,input().split())
year = 1
e,s,m = 1,1,1
while abs(E-e) or abs(S-s) or abs(M-m):
    year +=1
    e+=1
    s+=1
    m+=1
    if e>15:
        e-=15
    if s>28:
        s-=28
    if m>19:
        m-=19
print(year)
