s = input()
while s !="#":
    c = s[0]
    ans = 0
    for k in s[2:].lower():
        if c == k:
            ans +=1
    print(c,ans)
    s = input()
