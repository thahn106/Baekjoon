for k in range(int(input())):
    P,M = map(int,input().split())
    A = set()
    ans = 0
    M = [int(input()) for m in range(P)]
    for m in M:
        if m in A:
            ans +=1
        else:
            A.add(m)
    print(ans)
