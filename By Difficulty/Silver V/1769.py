X = int(input())
ans = 0
while X >= 10:
    X = sum(list(map(int, list(str(X)))))
    ans += 1
print(ans)
if X % 3:
    print("NO")
else:
    print("YES")
