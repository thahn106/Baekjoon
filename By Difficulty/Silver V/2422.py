N, M = map(int, input().split())

more = [0]*(N+1)
ban = set()
for m in range(M):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    more[a] += 1
    ban.add((a, b))

ans = 0
for a in range(1, N-1):
    for b in range(a+1, N):
        if (a, b) not in ban:
            for c in range(b+1,N+1):
                if ((a, c) not in ban) and ((b, c) not in ban):
                    ans +=1
print(ans)
