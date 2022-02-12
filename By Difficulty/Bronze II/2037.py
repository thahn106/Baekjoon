p,w = map(int,input().split())
s = input()
ans = 0
cur = 0
loc = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
count = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]
for c in s:
    if c == ' ':
        cur = 0
        ans += p
    else:
        d = ord(c)-65
        if loc[d]==cur:
            ans += w
        else:
            cur = loc[d]
        ans += count[d]*p
print(ans)
