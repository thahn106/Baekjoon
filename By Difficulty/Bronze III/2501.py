N,K = map(int,input().split())
divs = []
for i in range(N):
    if N%(i+1)==0:
        divs.append(i+1)
if K>len(divs):
    print(0)
else:
    print(divs[K-1])
