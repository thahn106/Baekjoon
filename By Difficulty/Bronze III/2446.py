N = int(input())
for j in range(1,2*N):
    i =abs(N-j)
    print(" "*(N-i-1)+"*"*(2*i+1))
