li = []
for n in range(int(input())):
    x,y = map(int,input().split())
    li.append((x,y))

ans = 0
for x in range(100):
    for y in range(100):
        for a,b in li:
            if a<=x<a+10 and b<=y<b+10:
                ans+=1
                break
print(ans)
