from itertools import combinations
a = list(map(int, input().split()))[1:]
t = 0
while a:
    if t:
        print("")
    for row in combinations(a, 6):
        print(*row)
    t += 1
    a = sorted(list(map(int, input().split()))[1:])
