N,B = map(int,input().split())
if N:
    ans = ""
    while N:
        N,r = divmod(N,B)
        if r<10:
            r = str(r)
        else:
            r = chr(65+(r-10))
        ans += r
    ans = ans[::-1]
else:
    ans = '0'
print(ans)
