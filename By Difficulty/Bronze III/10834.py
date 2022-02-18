dir = 0
ans = 1
for i in range(int(input())):
    a,b,d = map(int,input().split())
    if d:
        dir = 1-dir
    ans = (ans*b)//a
print(dir,ans)
