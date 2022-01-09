ans = [-1 for i in range(26)]
for i,c in enumerate(input()):
    if ans[ord(c)-97]==-1:
        ans[ord(c)-97] = i
print(*ans)
