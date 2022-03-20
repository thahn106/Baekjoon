a = set()
for i in range(int(input())):
    a.add(input())

for p in a:
    if p[::-1] in a:
        l = len(p)
        print(l, p[l//2])
        break
