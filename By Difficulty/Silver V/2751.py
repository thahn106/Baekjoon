import sys
input = sys.stdin.buffer.readline

N = int(input())
A = [0 for i in range(N)]
for n in range(N):
    A[n]=int(input())
A.sort()
for n in range(N):
    print(A[n])
