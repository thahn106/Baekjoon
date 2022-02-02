N,W,H = map(int,input().split())
for i in range(N):
    if int(input())**2 <= W*W+H*H:
        print("DA")
    else:
        print("NE")
