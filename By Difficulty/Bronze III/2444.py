N = int(input())
for j in range(1,2*N):
    i =abs(N-j)
    print(" "*(i)+"*"*(2*(N-i)-1))
