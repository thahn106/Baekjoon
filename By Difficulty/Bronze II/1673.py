try:
    while True:
        n,k = map(int,input().split())
        ans = 0
        s = 0
        while n:
            ans += n
            s += n
            n,s = divmod(s,k)
        print(ans)

except EOFError as e:
    pass
