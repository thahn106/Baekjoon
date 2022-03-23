e,f,c = map(int,input().split())
e +=f
ans = 0
while e>=c:
    d,e = divmod(e,c)
    e += d
    ans += d
print(ans)
