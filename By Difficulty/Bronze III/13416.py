for t in range(int(input())):
    ans = 0
    for N in range(int(input())):
        ans += max(0, max(list(map(int,input().split()))))
    print(ans)
