ans = 1
for c in input():
    if c=='A':
        if ans == 1:
            ans = 2
        elif ans == 2:
            ans = 1
    elif c == 'B':
        if ans == 3:
            ans = 2
        elif ans == 2:
            ans = 3
    else:
        if ans == 1:
            ans = 3
        elif ans == 3:
            ans = 1
print(ans)
