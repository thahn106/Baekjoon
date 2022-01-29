A = list(map(int,input().split()))
A.sort()
if A[1]-A[0] == A[2]-A[1]:
    print(2*A[2]-A[1])
elif A[1]-A[0] > A[2]-A[1]:
    print(2*A[1]-A[2])
else:
    print(2*A[1]-A[0])
