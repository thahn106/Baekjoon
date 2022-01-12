K,N = map(int,input().split())
lans = []
for k in range(K):
    lans.append(int(input()))
start = 0
end = (sum(lans)//N)+1
while start < end-1:
    mid = (start+end)//2
    temp = 0
    for k in lans:
        temp += k//mid
    if temp>=N:
        start = mid
    else:
        end = mid
print(start)
