for t in range(int(input())):
    s = input()
    N = int(s)
    if str(N*N)[-(len(s)):]==s:
        print("YES")
    else:
        print("NO")
