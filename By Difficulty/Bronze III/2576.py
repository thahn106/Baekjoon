odds = []
for i in range(7):
    n = int(input())
    if n%2:
        odds.append(n)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
