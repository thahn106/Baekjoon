ans = ""
for c in input():
    ans += chr(((ord(c)-68)%26)+65)
print(ans)
