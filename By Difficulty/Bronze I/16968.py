ans = 1
last = ''
for c in input():
    if c == 'c':
        if last == c:
            ans *= 25
        else:
            ans *= 26
    else:
        if last == c:
            ans *= 9
        else:
            ans *= 10
    last = c
print(ans)
