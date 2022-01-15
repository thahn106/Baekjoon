from math import floor
N,L,W,H = map(int,input().split())

start = 0
end = max(L,W,H)
for i in range(20000):
    m = (start+end)/2
    if floor(L/m)*floor(W/m)*floor(H/m) >=N:
        start = m
    else:
        end = m
print(float(end))
