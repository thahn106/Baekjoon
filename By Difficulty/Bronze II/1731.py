N = int(input())
A = [int(input()) for i in range(N)]

add = (A[2]-A[1]==A[1]-A[0])
if add:
    Q = A[2]-A[1]
    print(A[-1]+Q)
else:
    Q = A[2]//A[1]
    print(A[-1]*Q)
