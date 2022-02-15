d = int("".join(sorted(list(input()), reverse=True)))
if d%30:
    print(-1)
else:
    print(d)
