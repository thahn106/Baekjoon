ans = 0
for i in range(1, int(input())+1):
    s = str(i)
    for c in s:
        if c in "369":
            ans +=1
print(ans)
