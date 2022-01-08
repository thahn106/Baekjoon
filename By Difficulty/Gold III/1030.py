s, N, K, R1, R2, C1, C2 = map(int,input().split())
E = (N-K)//2

def color(x,y,s):
    if s == 0:
        return 0
    px,rx = divmod(x,N)
    py,ry = divmod(y,N)
    if color(px,py,s-1) == 1:
        return 1
    elif E<=rx<N-E and E<=ry<N-E:
        return 1
    else:
        return 0


for y in range(R1,R2+1):
    row = ""
    for x in range(C1,C2+1):
        row+=str(color(x,y,s))
    print(row)
