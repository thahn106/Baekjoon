ans = -1
for t in range(int(input())):
    a,b = map(int, input().split())
    if a<=b:
        if ans == -1:
            ans = b
        else:
            ans = min(ans, b)
print(ans)