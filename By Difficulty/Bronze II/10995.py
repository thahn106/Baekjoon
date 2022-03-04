N = int(input())
st = "*" + " *" * (N-1)
for i in range(N):
    if i%2:
        print(" "+st)
    else:
        print(st)