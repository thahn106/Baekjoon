ans = 0
words = set()
for i in range(int(input())):
    a = input()
    if a not in words:
        ans +=1
        for i in range(len(a)):
            b = a[i:]+a[:i]
            words.add(b)
print(ans)
