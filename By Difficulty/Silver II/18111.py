N, M, B = map(int,input().split())
grid = []
for i in range(N):
    grid += list(map(int,input().split()))
grid.sort()

ans = 500*500*256*2
h = -1
B += sum(grid)
time = 2*(sum(grid)+N*M)
j =0
for i in range(257):
    time -= 2*(N*M-j)
    time += 1*j
    while j < N*M and grid[j]<=i:
        j+=1
    # print("i:{} B:{} time:{}".format(i,B,time))
    if B>=0:
        if time <= ans:
            ans = time
            h = i
    else:
        break
    B -= N*M
print("{} {}".format(ans, h))
