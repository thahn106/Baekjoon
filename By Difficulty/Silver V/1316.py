ans = 0
for i in range(int(input())):
    found = [False for i in range(26)]
    cur = '-'
    good = True
    for c in input():
        if c !=cur:
            if found[ord(c)-97]:
                good =False
                break
            else:
                found[ord(c)-97] =True
                cur = c
    if good:
        ans += 1
print(ans)
