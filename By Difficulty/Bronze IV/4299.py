A,B =map(int,input().split())
f = (A+B)/2
s = (A-B)/2
if not(f==(A+B)//2 and s==(A-B)//2 and f>=0 and s>=0):
    print(-1)
else:
    print("{} {}".format(int(f),int(s)))
