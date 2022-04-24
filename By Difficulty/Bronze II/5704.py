s = input()
while s != "*":
    found = [0]*26
    for c in s:
        d = ord(c)
        if 97 <= d < 97+26:
            found[d-97] = 1
    if sum(found) == 26:
        print('Y')
    else:
        print('N')
    s = input()
