ans = 0
for i in range(8):
    s = input()
    for j in range(8):
        if (i+j)%2==0 and s[j]=='F':
            ans +=1
print(ans)
