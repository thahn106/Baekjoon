import sys
input = sys.stdin.readline

N = int(input())
A = [0 for i in range(N)]
for n in range(N):
    age, name = input().split()
    A[n]= (int(age),n,name.strip())
A.sort()
for n in range(N):
    print("{} {}".format(A[n][0],A[n][2]))
