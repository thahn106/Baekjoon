A = list(map(int,input().split()))
B = list(map(int,input().split()))

a,b = 0,0
for i in range(10):
    if A[i]>B[i]:
        a += 1
    elif A[i]<B[i]:
        b+=1
if a>b:
    print("A")
elif b>a:
    print("B")
else:
    print("D")
