try:
    while True:
        a = input()
        b = input()
        ac = [0 for i in range(26)]
        bc = [0 for i in range(26)]
        for c in a:
            ac[ord(c)-97]+=1
        for c in b:
            bc[ord(c)-97]+=1
        ans = ""
        for i in range(26):
            ans += chr(i+97)*min(ac[i],bc[i])
        print(ans)

except EOFError as e:
    pass
