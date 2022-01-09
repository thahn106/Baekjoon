L = int(input())
S = list(map(int,input().split()))
N = int(input())

S.sort()
rest = S[-1]+1

ans = S.copy()

dl = []
if S[0]==2:
    ans.append(1)
elif S[0]>2:
    dl.append((S[0]-1,1))
for i in range(L-1):
    d = S[i+1]-S[i]-1
    if d==1:
        ans.append(S[i]+1)
    else:
        dl.append((d,S[i]+1))
ans.sort()

def good(i,d):
    return i*(d-1-i)+d-1

looking  = (len(ans) < N)
dli = 0
dli = [0 for i in range(len(dl))]
while looking:
    mind = -1
    cand = 0
    candi = -1
    for i in range(len(dl)):
        j = dli[i]
        if j<dl[i][0]:
            if j%2:
                ind = dl[i][0]-1-(j//2)
            else:
                ind = (j//2)
            d = good(ind,dl[i][0])
            if d < mind or mind == -1:
                mind = d
                cand = dl[i][1]+ind
                candi = i
            elif d == mind and dl[i][1]+ind < cand:
                cand = dl[i][1]+ind
                candi = i
    if cand:
        ans.append(cand)
        dli[candi]+=1

    if not cand or len(ans) == N:
        looking = False

while (len(ans)< N):
    ans.append(rest)
    rest+=1

print(*ans[:N])
