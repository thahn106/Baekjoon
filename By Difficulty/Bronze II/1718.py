s = input()
k = input()
ans =""
for i in range(len(s)):
    d = k[i%(len(k))]
    if s[i]==" ":
        ans += ' '
    else:
        c = (ord(s[i])-ord(d)-1)%26
        ans += chr(c+97)
print(ans)
