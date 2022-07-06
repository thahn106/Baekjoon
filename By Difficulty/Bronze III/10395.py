ans = 'Y'
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for x, y in zip(a, b):
    if x+y != 1:
        ans = 'N'
print(ans)
