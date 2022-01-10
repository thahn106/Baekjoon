import sys
input = sys.stdin.readline

N = int(input())
A = [0 for i in range(N)]
for n in range(N):
    x,y =  map(int, input().split())
    A[n]= (x,y)
    
A.sort()
for n in range(N):
    print("{} {}".format(A[n][0],A[n][1]))
