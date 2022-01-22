x,y=0,0
recent = "D"
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for a,b in zip(A,B):
    if a>b:
        x+=3
        recent = "A"
    elif b>a:
        y+=3
        recent = "B"
    else:
        x+=1
        y+=1
print("{} {}".format(x,y))
if x>y:
    print("A")
elif y>x:
    print("B")
else:
    print(recent)
