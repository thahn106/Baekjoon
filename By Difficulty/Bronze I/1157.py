s = input().lower()
count = [0 for i in range(26)]
for c in s:
    count[ord(c)-97]+=1
m = max(count)
ans = 0
for i in range(26):
    if count[i] == m:
        if ans == 0:
            ans = chr(i+65)
        else:
            ans = "?"
print(ans)
