ans = 0
cur = ''
for c in input():
    if c==cur:
        ans +=5
    else:
        cur = c
        ans += 10
print(ans)
