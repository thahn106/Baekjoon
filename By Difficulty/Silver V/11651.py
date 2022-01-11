import sys
input = sys.stdin.buffer.readline

N = int(input())
c = [(0,0) for i in range(N)]
for n in range(N):
    x,y = map(int,input().split())
    c[n] = (y,x)

c.sort()
for y,x in c:
    sys.stdout.write(str(x)+" "+str(y)+"\n")
