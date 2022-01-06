s = input()
ans = 0
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        a = s[:i]
        b = s[i:j]
        c = s[j:]
        temp = a[::-1]+b[::-1]+c[::-1]
        if ans == 0:
            ans = temp
        elif temp < ans:
            ans = temp
print(ans)
