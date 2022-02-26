N = int(input())

ans  = 0
while N>1:
    ans += 1
    if N%2:
        N = 3*N+1
    else:
        N = N//2
        
print(ans)
