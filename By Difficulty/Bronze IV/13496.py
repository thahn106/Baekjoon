for k in range(int(input())):
    n, s, d = map(int, input().split())
    D = s*d
    ans = 0
    for i in range(n):
        d, v = map(int, input().split())
        if d <= D:
            ans += v
    if k:
        print("")
    print(f"Data Set {k+1}:")
    print(ans)
