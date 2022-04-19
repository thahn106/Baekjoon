for t in range(int(input())):
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(m)]
    ans = 0
    for i in range(n):
        run = 0
        for j in range(m):
            if grid[j][i]:
                run += 1
            else:
                ans += run
    print(ans)
