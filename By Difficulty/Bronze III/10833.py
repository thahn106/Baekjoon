ans = 0
for n in range(int(input())):
    A, B = map(int,input().split())
    ans += B%A
print(ans)
