h,w = map(int,input().split())
print(max(min(h,w)/2, min(h/3,w), min(h,w/3)))
