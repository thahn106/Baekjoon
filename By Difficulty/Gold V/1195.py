top = list(map(int,list(input())))
a = len(top)
bot = list(map(int,list(input())))
b = len(bot)
ans = a+b
for offset in range(-b,a):
    possible = True
    for i in range(min(offset,0), max(a, b+offset)):
        t = 0
        if 0<=i<a:
            t+=top[i]
        if 0<=i-offset<b:
            t+=bot[i-offset]
        if t>3:
            possible = False
            break
    if possible:
        ans = min(ans, max(a, b+offset)-min(offset,0))
print(ans)
