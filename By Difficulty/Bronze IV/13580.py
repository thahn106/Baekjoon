A = sorted(list(map(int, input().split())))
if A[0]==A[1] or A[1]==A[2] or A[0]+A[1]==A[2]:
    print("S")
else:
    print("N")
