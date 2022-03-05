M, N = map(int, input().split())
ans = 0
dir = 1
M -= 1
while M and N:
    if dir:
        N -= 1
        ans += 1
    else:
        M -= 1
        ans += 1

    dir = 1-dir
print(ans)
