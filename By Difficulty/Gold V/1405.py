steps,E,W,S,N = map(int,input().split())
P = [N,W,S,E]
dir = [(0,1),(-1,0),(0,-1),(1,0)]

def dfs(remaining, visited, pos, val, last_dir):
    x,y = pos
    ans = 0
    for i in range(3+int(remaining==steps-1)):
        next_dir = (last_dir+3+i)%4
        if P[next_dir]:
            dx,dy = dir[next_dir]
            newpos = (x+dx,y+dy)
            if newpos not in visited:
                if remaining:
                    VC = visited.copy()
                    VC.add(newpos)
                    ans += dfs(remaining-1,VC,newpos,val*P[next_dir],next_dir)
                else:
                    ans += val*P[next_dir]
    return ans

S = set()
S.add((0,0))
ans = dfs(steps-1,S,(0,0),1,1)
print(ans/(100**steps))
