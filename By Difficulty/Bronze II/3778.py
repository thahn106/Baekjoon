for test in range(int(input())):
    s = input()
    t = input()
    cs = [0]*26
    ct = [0]*26
    for c in s:
        cs[ord(c)-97]+=1
    for c in t:
        ct[ord(c)-97]+=1
    ans = 0
    for i in range(26):
        ans += max(cs[i],ct[i])-min(cs[i],ct[i])
    print(f"Case #{str(test+1)}: {str(ans)}")
