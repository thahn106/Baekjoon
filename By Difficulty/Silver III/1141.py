N = int(input())
words = []
for i in range(N):
    words.append(input())
words.sort()

ans = 0
prev = "$"
for word in words:
    if prev not in word:
        ans +=1
    elif word[:len(prev)] != prev:
        ans +=1
    prev = word
print(ans)
