for n in range(int(input())):
    s, a, b, c = map(int, input().split())
    d = a+b+c
    if 2*a >= 21 and 2*b >= 15 and c >= 12 and d>=55:
        ans = 'PASS'
    else:
        ans = 'FAIL'
    print(s, d, ans)
