a = sorted(list(map(int, input().split())))
print(a[0]+a[1]+min(a[0]+a[1]-1, a[2]))
