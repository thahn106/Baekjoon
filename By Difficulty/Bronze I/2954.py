s = input()
ans = ""
i = 0
while i < len(s):
    c = s[i]
    ans += c
    if c in 'aeiou':
        i += 3
    else:
        i += 1
print(ans)
