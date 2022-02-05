A,B = 0,0
for i in range(int(input())):
    a,b = map(int,input().split())
    if a>b:
        A+=1
    elif b>a:
        B+=1

print("{} {}".format(A,B))
