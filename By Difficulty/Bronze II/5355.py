for i in range(int(input())):
    s = input().split()
    cur = float(s[0])
    for c in s[1:]:
        if c == "@":
            cur*=3
        elif c == "%":
            cur += 5
        else:
            cur -= 7
    print(f"{cur:.2f}")
