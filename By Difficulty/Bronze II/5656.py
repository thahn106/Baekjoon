t = 1
while True:
    a, o, b = input().split()
    a, b = int(a), int(b)
    if o == '!=':
        ans = (a != b)
    elif o == '==':
        ans = (a == b)
    elif o == '<=':
        ans = (a <= b)
    elif o == '<':
        ans = (a < b)
    elif o == '>=':
        ans = (a >= b)
    elif o == '>':
        ans = (a > b)
    else:
        break
    print(f"Case {t}: {str(ans).lower()}")
    t += 1
