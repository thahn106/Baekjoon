N = int(input())
for j in range(1,2*N):
    i = abs(N-j)
    print("*"*((N-i))+" "*(2*i)+"*"*((N-i)))
