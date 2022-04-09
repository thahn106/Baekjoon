N = input()
while N != '0':
    b,p,m = N.split()
    b = int(b)
    p = int(p,b)
    m = int(m,b)
    q = p%m
    ans = ""
    while q:
        q,r = divmod(q,b)
        ans+=str(r)
    if not ans:
        ans = '0'
    print(int(ans[::-1]))
    N = input()
