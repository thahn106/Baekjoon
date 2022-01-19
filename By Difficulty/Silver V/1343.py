s = input()
start = -1
valid = True
ans = ""
for i,c in enumerate(s):
    if c=="X" and start == -1:
        start = i
    if c=='.':
        if start != -1:
            if (i-start) % 2:
                valid = False
                break
            d,r = divmod(i-start,4)
            ans += "AAAA"*d
            if r:
                ans +="BB"
        ans += '.'
        start = -1

if start != -1:
    if (len(s)-start)%2:
        valid = False
    d,r = divmod(len(s)-start,4)
    ans +="AAAA"*d
    if r:
        ans +="BB"

if valid:
    print(ans)
else:
    print(-1)
