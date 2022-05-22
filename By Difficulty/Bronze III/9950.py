l,w,a = map(int,input().split())
while l or w or a:
    if not l:
        l = a // w
    if not w:
        w = a // l
    if not a:
        a = w*l
    print(l,w,a)
    l,w,a = map(int,input().split())
