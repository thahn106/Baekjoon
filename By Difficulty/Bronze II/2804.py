X,Y = input().split()

found = False
for i,c in enumerate(X):
    for j,d in enumerate(Y):
        if c == d:
            x,y = i,j
            found = True
            break
    if found:
        break

for j,d in enumerate(Y):
    row = ""
    for i,c in enumerate(X):
        if i == x:
            row +=d
        elif j == y:
            row+=c
        else:
            row+='.'
    print(row)
