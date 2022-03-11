def rot(c):
    if 64<ord(c)<96:
        return chr((ord(c)-65+13)%26+65)
    elif 96<ord(c)<128:
        return chr((ord(c)-97+13)%26+97)
    else:
        return c


s = input()
ans = ""
for c in s:
    ans += rot(c)
print(ans)
