counts = [0 for i in range(26)]
try:
    while True:
        s = input()
        for c in s:
            if c ==" ":
                pass
            else:
                counts[ord(c)-97]+=1
except EOFError as e:
    pass

m = max(counts)
ans = ""
for i in range(26):
    if counts[i]==m:
        ans += chr(i+97)
print(ans)
