from bisect import bisect_left
N = int(input())
cw = sorted(list(map(int,input().split())), reverse = True)
M = int(input())
bw = sorted(list(map(int,input().split())), reverse = True)

if max(bw)>max(cw):
    print(-1)
else:
    ans = 0
    maxb = N
    while bw:
        ans +=1
        i = 0
        for n,crane in enumerate(cw[:maxb]):
            while i<len(bw):
                if bw[i]<=crane:
                    bw.remove(bw[i])
                    break
                else:
                    i+=1
            if i>=len(bw):
                maxb = n
    print(ans)
