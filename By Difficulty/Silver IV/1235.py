N = int(input())
students = [input() for i in range(N)]
m = len(students[0])
for i in range(m):
    a = {}
    working = True
    for c in students:
        if c[-(i+1):] not in a:
            a[c[-(i+1):]] = True
        else:
            working = False
            break
    if working:
        print(i+1)
        break
