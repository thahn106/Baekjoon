N,x,y = map(int,input().split())
col = []

for i in range(N):
    a = list(map(int,input().split()))
    col.append(a[y-1])
    if i == x-1:
        row = a
j = row[y-1]
if j == max(row) and j == max(col):
    print("HAPPY")
else:
    print("ANGRY")
