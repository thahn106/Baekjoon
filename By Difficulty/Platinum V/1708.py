import sys
input = sys.stdin.buffer.readline

from functools import cmp_to_key

class Point:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __str__(self):
        return ("(" + str(self.x) + ", " + str(self.y) + ")")

p0 = Point(0,0)

def orientation(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) -
           (q.x - p.x) * (r.y - q.y))
    if val == 0:
        return 0    #col
    elif val > 0:
        return -1   #cw
    else:
        return 1    #ccw

def disq(p,q): return (p.y-q.y)**2+(p.x-q.x)**2

def cmp(p,q):
    o = orientation(p0, p, q)
    if o == 0:
        if disq(p0, q)>=disq(p0,p):
            return -1
        else:
            return 1
    else:
        if o == 1:
            return -1
        else:
            return 1

def convexHull(points, n):
    global p0
    p0 = points[0]
    points = sorted(points, key = cmp_to_key(cmp))

    m = 1
    for i in range(1, n):

        while ((i < n - 1) and (orientation(p0, points[i], points[i+1]) == 0)):
            i += 1
        points[m] = points[i]
        m += 1

    if m < 3:
        return
    S = []
    for i in range(3): S.append(points[i])

    for i in range(3, m):
        while ((len(S) > 1) and (orientation(S[-2], S[-1], points[i]) != 1)):
            S.pop()
        S.append(points[i])
    return S

N = int(input())
points = []
for n in range(N):
    x,y = map(int,input().split())
    points.append((y,x))
points.sort()

for n in range(N):
    y,x = points[n]
    points[n]= Point(x,y)
S = convexHull(points,N)
print(len(S))
