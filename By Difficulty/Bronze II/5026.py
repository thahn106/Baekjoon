for i in range(int(input())):
    s = input()
    if '+' in s:
        a, b = map(int, s.split('+'))
        print(a+b)
    else:
        print("skipped")
