def spiral(r,c):
    n = max(abs(r),abs(c))
    m = (2*n+1)
    M = m**2
    if r == n:
        return M-n+c
    elif c == -n:
        return M-3*n+r
    elif r == -n:
        return M-5*n-c
    else:
        return M-7*n-r

r1,c1,r2,c2 = map(int,input().split())
ans = []
l = 1
for r in range(r1,r2+1):
    row = []
    for c in range(c1,c2+1):
        temp = str(spiral(r,c))
        l = max(l, len(temp))
        row.append(temp)
    ans.append(row)

for row in ans:
    for i in range(len(row)):
        row[i] = (" "*(l-len(row[i])))+row[i]
    print(*row)
