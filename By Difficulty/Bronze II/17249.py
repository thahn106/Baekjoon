L, R = 0, 0
right = False
for c in input():
    if c == '@':
        if right:
            R += 1
        else:
            L += 1
    elif c == "0":
        right = True
print(L, R)
