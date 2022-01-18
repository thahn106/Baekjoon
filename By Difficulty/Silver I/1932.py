n = int(input())
rows = []
for i in range(n):
    rows.append(list(map(int,input().split())))

for i in range(1,n):
    cr = n-i
    for j in range(cr):
        rows[cr-1][j] += max(rows[cr][j],rows[cr][j+1])
print(rows[0][0])
