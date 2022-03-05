N, G = map(int, input().split())
rooms = [0]*N
i = 0
full = False
for g in range(G):
    t = int(input())
    while t and not full:
        a = min(2, t)
        rooms[i] = a
        t -= a
        i += 1
        if i >= N:
            full = True
            i = 0
    while t:
        while rooms[i] == 2:
            i += 1
        rooms[i] += 1
        t -= 1
for r in rooms:
    print(r)
