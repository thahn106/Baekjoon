from math import ceil
rh, rv, sh, sv = map(int,input().split())
ans = 10000**5
for i in range(int(input())):
    rhi, rvi, shi, svi, pi = map(int,input().split())
    r = ceil(max(rh/rhi,sh/shi))
    c = ceil(max(rv/rvi,sv/svi))
    ans = min(r*c*pi, ans)
    r = ceil(max(rv/rhi,sv/shi))
    c = ceil(max(rh/rvi,sh/svi))
    ans = min(r*c*pi, ans)
print(ans)
