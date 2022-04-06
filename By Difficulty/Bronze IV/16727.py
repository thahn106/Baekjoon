p1,s1 = map(int,input().split())
s2,p2 = map(int,input().split())
P = "Persepolis"
S = "Esteghlal"
if p1+p2>s1+s2:
    print(P)
elif p1+p2<s1+s2:
    print(S)
else:
    if s1>p2:
        print(S)
    elif s1<p2:
        print(P)
    else:
        print("Penalty")
