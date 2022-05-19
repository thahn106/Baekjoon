for t in range(int(input())):
    N, D = map(int, input().split())
    ans = 0
    for n in range(N):
        v,f,c = map(int,input().split())
        if D*c <= f*v:
            ans += 1
    print(ans)
