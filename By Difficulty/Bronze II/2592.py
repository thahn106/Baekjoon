s = [int(input()) for i in range(10)]
s.sort()
print(sum(s)//10)
m = 0
ans = []
cur = 0
n = 0
for i in s:
    if cur ==i:
        n +=1
    else:
        if n>m:
            m = n
            ans = [cur]
        elif n == m:
            ans.append(cur)
        n = 1
        cur = i
if n>m:
    m = n
    ans = [cur]
elif n == m:
    ans.append(cur)
print(ans[0])
