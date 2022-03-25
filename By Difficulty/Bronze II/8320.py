from math import sqrt, floor
ans = 0
n = int(input())
for i in range(1,floor(sqrt(n))+1):
    ans += max(0, (n//i) -i+1)
print(ans)
