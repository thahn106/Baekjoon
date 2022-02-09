a,b,c = map(int,input().split())
counts = [0 for i in range(a+b+c+1)]

for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1, c+1):
            counts[i+j+k]+=1
m =max(counts)

for i in range(a+b+c+1):
    if counts[i]==m:
        print(i)
        break
