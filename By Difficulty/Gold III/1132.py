A = [0 for i in range(10)]
F = [False for i in range(10)]
for n in range(int(input())):
    S = input()
    D = len(S)
    for i in range(D):
        if i==0:
            F[ord(S[i])-65] = True
        A[ord(S[D-1-i])-65] += 10**i

Zc = max(A)+1
for i in range(10):
    if not F[i]:
        if A[i] < Zc:
            Z = i
            Zc = A[i]
A = A[:Z]+A[Z+1:]

A.sort()
ans = 0
for i in range(1,10):
    ans += i*A[i-1]
print(ans)
