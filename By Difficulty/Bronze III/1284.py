s = input()
while s != "0":
    ans = len(s)+1
    for c in s:
        if c == "1":
            ans +=2
        elif c == "0":
            ans +=4
        else:
            ans +=3
    print(ans)
    s = input()
