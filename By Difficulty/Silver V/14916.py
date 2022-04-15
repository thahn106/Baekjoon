n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    q, d = divmod(n, 5)
    print(q+[0, 2, 1, 3, 2][d])
