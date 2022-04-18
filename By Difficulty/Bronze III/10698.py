for t in range(int(input())):
    x, o, y, e, z = input().split()
    x, y, z = int(x), int(y), int(z)
    if o == '+':
        if x+y == z:
            ans = 'YES'
        else:
            ans = 'NO'
    else:
        if x-y == z:
            ans = 'YES'
        else:
            ans = 'NO'
    print(f"Case {t+1}: {ans}")
