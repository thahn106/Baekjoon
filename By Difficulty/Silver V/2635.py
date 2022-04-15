n = int(input())
ans = [n]
for i in range(1, n+1):
    temp = [n, i]
    while temp[-2] >= temp[-1]:
        temp.append(temp[-2]-temp[-1])
    if len(temp) > len(ans):
        ans = temp
print(len(ans))
print(*ans)
