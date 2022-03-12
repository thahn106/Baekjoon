V = int(input())
s = input()
A = 0
B = 0
for c in s:
    if c=='A':
        A+=1
    else:
        B+=1
if A>B:
    print("A")
elif B>A:
    print("B")
else:
    print("Tie")
