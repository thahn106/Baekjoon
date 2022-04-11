n = int(input())
s = input()

ans = 0
bonus = 0
for i, c in enumerate(s):
    if c == 'O':
        ans += i+1
        ans += bonus
        bonus += 1
    else:
        bonus = 0
print(ans)
