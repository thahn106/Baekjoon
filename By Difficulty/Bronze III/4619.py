from math import pow, floor
B,N = map(int,input().split())
while B or N:
    A = floor(pow(B,1/N))
    if abs(B-pow(A,N)) <= abs(B-pow(A+1,N)):
        print(A)
    else:
        print(A+1)
    B,N = map(int,input().split())
