s = input()
while s != "#":
    ref =["/", "-", '\\', '(', '@', '?', '>','&','%']
    ans = 0
    for j in range(len(s)):
        for i in range(9):
            if s[j] == ref[i]:
                ans +=  (i-1)*(8**(len(s)-1-j))
    print(ans)
    s = input()
