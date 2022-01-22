N = int(input())
for i in range(2*N-1):
    j = abs(N-1-i)
    print(" "*j+"*"*(N-j))
