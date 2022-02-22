from itertools import product

N = int(input())
M = int(input())
a = []
if M:
    a = input().split()

b = list(map(str,range(10)))
B = list(set(b)-set(a))

# print(B)
ans = abs(100-N)
for i in range(1,7):
    if i>ans:
        break
    for but in product(B, repeat=i):
        n = int("".join(but))
        ans = min(ans, i+abs(n-N))
print(ans)
