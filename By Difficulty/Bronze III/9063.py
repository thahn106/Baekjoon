xa = -10000
ya = -10000
xi = 10000
yi = 10000
for n in range(int(input())):
    x, y = map(int, input().split())
    xa = max(xa, x)
    xi = min(xi, x)
    ya = max(ya, y)
    yi = min(yi, y)
print((xa-xi)*(ya-yi))
