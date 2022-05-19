L, D, X = [int(input()) for i in range(3)]

N = D
M = L

for l in range(L,D+1):
    if sum(list(map(int, list(str(l))))) == X:
        N = min(N,l)
        M = max(M,l)
print(N)
print(M)
