def argmax(a, alive):
    m = min(a)-1
    ans = 0
    for i in range(len(a)):
        if alive[i] and a[i]>m:
            m = a[i]
            ans = i
    return ans

N = int(input())
a = list(map(int,input().split()))
R = []
for i in range(N):
    R.append(list(map(int,input().split())))
X = int(input())

def search(L,i,a,alive):
    if i == X:
        return 0
    alive[i] = False
    for n in range(N):
        a[n]+=R[i][n]
    nL = L-1
    vote = argmax(a, alive)
    alive[vote] = False
    nL -= 1
    if vote == X:
        return 0
    elif nL == 2:
        return 1
    else:
        ans = 0
        for i in range(N):
            if alive[i] and ans != nL//2:
                ans = max(ans, search(nL,i,a.copy(),alive.copy())+1)
        return ans

L = N
if L == 1:
    print(0)
else:
    alive = [True for i in range(N)]
    if L % 2:
        vote = argmax(a, alive)
        alive[vote] = False
        L -= 1
        if vote == X:
            print(0)
    if alive[X]:
        ans = 0
        for i in range(N):
            if alive[i] and ans != L//2:
                ans = max(ans, search(L,i,a.copy(),alive.copy())+1)
        print(ans)
