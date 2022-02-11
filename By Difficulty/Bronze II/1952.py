M,N = map(int,input().split())
M -= 1
ans = 0
dir = True
while M and N:
    ans +=1
    if dir:
        N -= 1
        dir = False
    else:
        M -= 1
        dir = True
print(ans)
