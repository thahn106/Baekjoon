N = int(input())
ans = 0
for i in range(1,500):
    for j in range(i+1,501):
        if j*j-i*i==N:
            ans += 1

print(ans)
