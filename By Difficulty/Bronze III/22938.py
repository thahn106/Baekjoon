x,y,r = map(int, input().split())
a,b,s = map(int, input().split())
if (x-a)**2+(y-b)**2 < (r+s)**2:
    print("YES")
else:
    print("NO")
