import math
D,H,W = map(int,input().split())
r = D/math.sqrt(H*H+W*W)
ans = [math.floor(r*H), math.floor(r*W)]
print(*ans)
