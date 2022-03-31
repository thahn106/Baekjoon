N,M = map(int,input().split())

balls = list(range(1,N+1))
for i in range(M):
    a,b = map(int,input().split())
    balls[a-1],balls[b-1] = balls[b-1],balls[a-1]

print(*balls)
