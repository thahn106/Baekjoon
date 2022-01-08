K,S,N = input().split()
x,y = ord(K[0])-64,int(K[1])
a,b = ord(S[0])-64,int(S[1])

for i in range(int(N)):
    M = input()
    dx,dy = 0,0
    for c in M:
        if c == "R":
            dx +=1
        elif c == "L":
            dx -= 1
        elif c =="T":
            dy +=1
        elif c =="B":
            dy -=1
    if 1<= x+dx <=8  and 1<= y+dy <=8:
        if x+dx == a and y+dy==b:
            if 1<= a+dx <=8  and 1<=b+dy<=8:
                a += dx
                b += dy
                x += dx
                y += dy
        else:
            x += dx
            y += dy
print(chr(x+64)+str(y))
print(chr(a+64)+str(b))
