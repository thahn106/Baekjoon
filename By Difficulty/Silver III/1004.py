def inside(first, second, dis):
    return (first[0]-second[0])**2+(first[1]-second[1])**2 < dis*dis

for t in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    start  = (x1,y1)
    end = (x2,y2)
    ans = 0
    for n in range(int(input())):
        xc,yc,r = map(int,input().split())
        if inside(start, (xc,yc), r)^inside(end, (xc,yc), r):
            ans+=1
    print(ans)
