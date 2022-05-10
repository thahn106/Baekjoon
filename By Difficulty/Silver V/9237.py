N = int(input())
t = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i, c in enumerate(t):
    ans = max(ans, i+c)
print(ans+2)
