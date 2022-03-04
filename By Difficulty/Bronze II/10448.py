tri = []
i = 1
while True:
    t = i*(i+1)//2
    if t > 1000:
        break
    tri.append(t)
    i += 1

for t in range(int(input())):
    n = int(input())
    possible = False
    for i in tri:
        for j in tri:
            if n-i-j in tri:
                possible = True
                break
        if possible:
            break
    print(int(possible))
