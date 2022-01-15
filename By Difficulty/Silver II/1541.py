s = input().split('-')
t = []
for i in s:
    t.append(sum([int(n) for n in i.split('+')]))

ans = 2*t[0]-sum(t)
print(ans)
