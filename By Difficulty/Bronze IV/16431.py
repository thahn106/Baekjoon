br,bc = map(int,input().split())
dr,dc = map(int,input().split())
jr,jc = map(int,input().split())

b = max(abs(jr-br), abs(jc-bc))
d = abs(jr-dr)+abs(jc-dc)

if b<d:
    print("bessie")
elif d<b:
    print("daisy")
else:
    print("tie")
