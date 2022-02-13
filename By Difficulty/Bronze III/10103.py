A = 100
B = 100
for n in range(int(input())):
    a,b = map(int,input().split())
    if a<b:
        A -= b
    elif b<a:
        B -= a
print(A)
print(B)
