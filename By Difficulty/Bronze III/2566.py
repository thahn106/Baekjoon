a = []
m = 0
for i in range(9):
    row = list(map(int,input().split()))
    m = max(m,max(row))
    a.append(row)
found = False
for i in range(9):
    for j in range(9):
        if a[i][j]==m:
            print(m)
            print("{} {}".format(i+1,j+1))
            found = True
            break
    if found: break
