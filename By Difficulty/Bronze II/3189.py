A, B, C = map(int, input().split())
cur = A
c = 10**len(str(C))
ans = 0
while ans < 100010:
    cur *= B
    ans += 1
    cur = cur % c
    if cur == C:
        break

if ans > 100000:
    print("NIKAD")
else:
    print(ans)
