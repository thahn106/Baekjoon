L,R,A = map(int,input().split())
D = max(L,R)-min(L,R)
rest = 0
if A>D:
    rest = (A-D)//2
print(min(L,R)*2+ min(D,A)*2+rest*2)
