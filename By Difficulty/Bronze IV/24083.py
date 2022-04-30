A = int(input())
B = int(input())
ans = (A+B) % 12
if not ans:
    ans += 12
print(ans)
