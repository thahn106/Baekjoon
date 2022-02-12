def om(li,ind):
    ans = 0
    for i in range(len(li)):
        if i!=ind:
            ans = max(ans, li[i])
    return ans


N,S = input().split()
N = int(N)
ms = [0]*N
ss = [0]*N
gs = [0]*N
for c in S:
    gw = False
    w = ord(c)-65
    if gs[w]==3 and om(gs,w)<=2:
        gw = True
    elif gs[w]==4:
        gw = True
    else:
        docked = False
        for i in range(N):
            if i != w and gs[i]==4:
                gs[i]-=1
                docked = True
        if not docked:
            gs[w]+=1
    if gw:
        sw = False
        gs = [0]*N
        ss[w]+=1
        if ss[w]>=6 and ss[w]-om(ss,w)>=2:
            sw = True
        if sw:
            ms[w]+=1
            if om(ss,w)==0:
                ms[w]+=1
            ss = [0]*N
            if ms[w]>=3:
                print(chr(w+65))
                break
