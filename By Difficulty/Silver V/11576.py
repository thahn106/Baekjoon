A, B = map(int, input().split())
M = int(input())
a = list(map(int, input().split()))
a.reverse()
val = 0
for i, d in enumerate(a):
    val += d*(A**i)

ans = []
while val:
    val, d = divmod(val, B)
    ans.append(d)

ans.reverse()
print(*ans)
