for t in range(int(input())):
    S = input()
    ans = 0
    cur = 0
    for c in S:
        if c == "O":
            cur +=1
            ans +=cur
        else:
            cur = 0
    print(ans)
