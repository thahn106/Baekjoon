R,B = map(int,input().split())
for L in range(1,5000):
    W = (R+4-2*L)/2
    if W == round(W) and W>0 and L*W == R+B:
        W = round(W)
        break

print(max(L,W), min(L,W))
