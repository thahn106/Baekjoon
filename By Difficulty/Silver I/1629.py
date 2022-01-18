A,B,C = map(int,input().split())

ans = 1
while B:
    if B%2:
        ans = (ans*A)%C
    B=B//2
    A = (A*A)%C
print(ans)
