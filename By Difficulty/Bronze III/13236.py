n = int(input())
ans = [n]
while n>1:
    if n%2:
        n = 3*n+1
    else:
        n = n//2
    ans.append(n)
print(*ans)
