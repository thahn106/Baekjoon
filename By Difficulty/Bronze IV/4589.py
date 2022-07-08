print("Gnomes:")
for n in range(int(input())):
    s = list(map(int, input().split()))
    if s == sorted(s) or s == sorted(s, reverse=True):
        print("Ordered")
    else:
        print("Unordered")
