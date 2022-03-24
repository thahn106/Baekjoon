L,P,V = map(int,input().split())
t = 1
while L or P or V:
    d,r = divmod(V, P)
    print(f"Case {t}: {d*L+min(r,L)}")
    L,P,V = map(int,input().split())
    t +=1
