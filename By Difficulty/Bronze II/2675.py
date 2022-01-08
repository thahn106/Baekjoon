for t in range(int(input())):
    R,S = input().split()
    ans = ""
    for c in S:
        ans += c*(int(R))
    print(ans)
