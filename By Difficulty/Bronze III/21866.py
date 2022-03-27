ref = [100,100,200,200,300,300,400,400,500]
m = list(map(int,input().split()))
hack = False
for r,a in zip(ref,m):
    if r<a:
        hack=True
if hack:
    print("hacker")
elif sum(m)>=100:
    print("draw")
else:
    print("none")
