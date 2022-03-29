a,b = 1,1
for i in range(1,int(input())):
    if a==1:
        a = b+1
        b = 1
    else:
        a -= 1
        b += 1
print(a,b)
