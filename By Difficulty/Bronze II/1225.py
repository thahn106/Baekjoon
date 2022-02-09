A,B = input().split()
A = list(map(int,list(A)))
B = list(map(int,list(B)))
ans = 0
for a in A:
    for b in B:
        ans += a*b
print(ans)
