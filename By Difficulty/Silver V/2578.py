grid = [0]*25
for i in range(5):
    a = list(map(int, input().split()))
    for j,c in enumerate(a):
        grid[c-1] = i*5+j

checked = [0]*25

def checkgrid():
    rows = 0
    for i in range(5):
        ref = [i+5*x for x in range(5)]
        t = 0
        for c in ref:
            t += checked[c]
        if t==5:
            rows += 1
    for i in range(5):
        ref = [5*i+x for x in range(5)]
        t = 0
        for c in ref:
            t += checked[c]
        if t == 5:
            rows +=1
    ref = [0,6,12,18,24]
    t = 0
    for c in ref:
        t += checked[c]
    if t==5:
        rows+=1
    ref = [4,8,12,16,20]
    t = 0
    for c in ref:
        t += checked[c]
    if t==5:
        rows +=1
    return rows >= 3

ans = 0
found = False
for i in range(5):
    a = list(map(int, input().split()))
    for j in a:
        checked[grid[j-1]]=1
        ans += 1
        if ans >= 12:
            found = checkgrid()
            if found:
                break
    if found:
        break
print(ans)
