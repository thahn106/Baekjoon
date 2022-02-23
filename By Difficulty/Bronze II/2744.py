s = list(input())
for i in range(len(s)):
    c = ord(s[i])
    if c>96:
        s[i] = chr(c-32)
    else:
        s[i] = chr(c+32)
print("".join(s))
