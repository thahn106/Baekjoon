ar = [1,0,0,2]
for c in input():
    if c == 'A':
        i,j = 0,1
    elif c == 'B':
        i,j = 0,2
    elif c == 'C':
        i,j = 0,3
    elif c == 'D':
        i,j = 1,2
    elif c == 'E':
        i,j = 1,3
    elif c == 'F':
        i,j = 2,3
    ar[i],ar[j] = ar[j],ar[i]

print(ar.index(1)+1)
print(ar.index(2)+1)
