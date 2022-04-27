A, B = map(int, input().split())
ans = []
for i in range(1, 50):
    ans += [i]*i
print(sum(ans[A-1:B]))
