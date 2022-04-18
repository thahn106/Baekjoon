scores = list(map(int, input().split()))
ans = 0
for i in range(int(input())):
    ts = 0
    for j in range(3):
        moves = list(map(int, input().split()))
        for a, b in zip(scores, moves):
            ts += a*b
    ans = max(ans, ts)
print(ans)
