for t in range(int(input())):
    s = input()
    n = len(s)//2
    if s[n] == s[n-1]:
        print("Do-it")
    else:
        print("Do-it-Not")
