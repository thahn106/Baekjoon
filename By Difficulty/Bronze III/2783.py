x,y = map(int,input().split())
m = 1000*x/y
for i in range(int(input())):
    x,y = map(int,input().split())
    m = min(m,1000*x/y)
print(m)
