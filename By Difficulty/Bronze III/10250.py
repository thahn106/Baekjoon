for t in range(int(input())):
    H, W, N = map(int,input().split())
    d,r = divmod(N-1,H)
    print((r+1)*100+d+1)
