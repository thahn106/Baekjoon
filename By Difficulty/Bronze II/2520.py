from math import floor
for t in range(int(input())):
    _ = input()
    cm, y, ssu, ssa, f = map(int,input().split())
    b, gs, gc, w = map(int,input().split())
    pancakes = min(floor(16*cm/8),floor(16*y/8),floor(16*ssu/4),floor(16*ssa/1),floor(16*f/9))
    print(min(pancakes, b+floor(gs/30)+floor(gc/25)+floor(w/10)))
