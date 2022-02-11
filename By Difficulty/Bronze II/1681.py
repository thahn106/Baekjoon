N,L = input().split()

cur = 0
for i in range(int(N)):
    cur +=1
    while L in str(cur):
        cur+=1
print(cur)
