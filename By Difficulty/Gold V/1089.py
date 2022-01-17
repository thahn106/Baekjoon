ref = ["###...#.###.###.#.#.###.###.###.###.###",
"#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
"#.#...#.###.###.###.###.###...#.###.###",
"#.#...#.#.....#...#...#.#.#...#.#.#...#",
"###...#.###.###...#.###.###...#.###.###"]

N = int(input())
rows = [input() for i in range(5)]

refs = [[ref[i][4*n:4*n+4] for i in range(5)]   for n in range(10)]
digits= [[rows[i][4*n:4*n+4] for i in range(5)]   for n in range(N)]

ans = 0
working = True

for i in range(N):
    cur = digits[i]
    posd = []
    for d in range(10):
        refd = refs[d]
        pos = True
        for r in range(5):
            for c in range(3):
                if cur[r][c] == '#' and refd[r][c]=='.':
                    pos = False
                    break
            if not pos:
                break
        if pos:
            posd.append(d)
    # print("i:{}".format(i))
    # print(posd)
    if posd:
        ans += (sum(posd)/len(posd))*10**(N-1-i)
    else:
        working = False
        break
if working:
    print(ans)
else:
    print(-1)
