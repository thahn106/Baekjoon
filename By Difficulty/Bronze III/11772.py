ans = 0
for i in range(int(input())):
    s = input()
    ans += int(s[:-1])**int(s[-1])
print(ans)
