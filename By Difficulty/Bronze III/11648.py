s = list(map(int, list(input())))
ans = 0
while len(s) > 1:
    temp = 1
    for i in s:
        temp *= i
    ans += 1
    s = list(map(int, list(str(temp))))
print(ans)
