N = int(input())
count = [0]*N
for i in range(N):
    count[i] = int(input())
cur = count[0]
start = count[0]
count[0]=0
count.sort(reverse=True)

for i in range(N-1):
    if cur > count[i]:
        break
    if (count[i]-count[i+1])*(i+1)+cur>count[i+1]:
        for j in range((count[i]-count[i+1])):
            if cur+(i+1) <= count[i]-1:
                cur+=(i+1)
                count[i]-=1
            else:
                if cur+(i+1)== count[i]:
                    cur = count[i]
                else:
                    cur = count[i]+1
                break
    else:
        cur += (count[i]-count[i+1])*(i+1)

print(cur-start)
