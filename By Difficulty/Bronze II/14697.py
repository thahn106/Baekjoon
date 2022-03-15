A,B,C,N = map(int,input().split())
a,b,c = 0,0,0
found = False
while c*C<=N:
    b = 0
    while b*B+c*C<=N:
        if (N-(b*B+c*C)) % A ==0:
            found = True
            break
        b+=1
    c+=1
    if found:
        break

print(int(found))
