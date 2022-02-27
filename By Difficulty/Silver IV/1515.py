s = input()
ans = ""
i = 0
while True:
    i+=1
    ans += str(i)
    k = 0
    for c in s:
        while k<len(ans) and ans[k]!=c:
            k+=1
        k+=1
    if k > len(ans):
        continue
    else:
        break
print(i)
