C,K = map(int,input().split())
b = 10**K
R,D = divmod(C,b)
if K:
    if not D<b//2:
        R+=1
print(R*b)
