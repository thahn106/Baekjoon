ref = 'SNU'
ans = 0
anc = 0
for i in range(3):
    a, b = map(int, input().split())
    p = 10*a
    if p >= 5000:
        p -= 500
    temp = 10*b / p
    if temp > ans:
        ans = temp
        anc = i
print(ref[anc])
