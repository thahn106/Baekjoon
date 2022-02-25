R = int(input())
s = input()
N = int(input())
grid = [input() for i in range(N)]
ans = 0
opt = 0
for i in range(R):
    ref = "".join([grid[j][i] for j in range(N)])
    rc = ref.count("R")
    pc = ref.count("P")
    sc = ref.count("S")
    rs = sc*2+rc
    ps = rc*2+pc
    ss = pc*2+sc
    if s[i] == 'S':
        ans+=ss
    elif s[i] == 'P':
        ans += ps
    else:
        ans += rs
    opt += max(rs,ps,ss)
print(ans)
print(opt)
