x, y = map(int, input().split())
r = [0, y]
c = [0, x]
for t in range(int(input())):
    a, p = map(int, input().split())
    if a:
        c.append(p)
    else:
        r.append(p)
r.sort()
c.sort()
rm = 0
for i in range(1,len(r)):
    rm = max(rm, r[i]-r[i-1])
cm = 0
for i in range(1,len(c)):
    cm = max(cm, c[i]-c[i-1])
print(rm*cm)
