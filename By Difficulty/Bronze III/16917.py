A, B, C, X, Y = map(int,input().split())

if A+B <= 2*C:
    print(A*X+B*Y)
else:
    d = min(X,Y)
    X -= d
    Y -= d
    ans = d*2*C
    if X:
        if A<2*C:
            ans += A*X
        else:
            ans += 2*C*X
    if Y:
        if B<2*C:
            ans += B*Y
        else:
            ans += 2*C*Y
    print(ans)
