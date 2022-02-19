Ad,Ah=map(int,input().split())
Bd,Bh=map(int,input().split())
while Ah and Bh:
    Ah = max(0, Ah-Bd)
    Bh = max(0, Bh-Ad)

if Ah:
    print("PLAYER A")
elif Bh:
    print("PLAYER B")
else:
    print("DRAW")
