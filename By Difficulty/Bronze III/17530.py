N = int(input())
A = [int(input()) for i in range(N)]
if A[0]==max(A):
    print("S")
else:
    print("N")
