N = int(input())
s = input()
l = False
ans = 0
i = 0
while i<N:
    ans += 1
    if s[i]=='S':
        i+=1
    else:
        i+=2
        if not l:
            l = True
            ans += 1
print(ans)
