s = input()
i = 1
while s != '0':
    r, w, l = map(int, s.split())
    ans = "fits"
    if l*l+w*w > 4*r*r:
        ans = "does not fit"
    print(f"Pizza {i} {ans} on the table.")
    i += 1
    s = input()
