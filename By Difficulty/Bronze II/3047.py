A = list(map(int,input().split()))
A.sort()
ans  = []
for c in input():
    if c == 'A':
        ans.append(A[0])
    elif c == 'B':
        ans.append(A[1])
    else:
        ans.append(A[2])
print(*ans)
