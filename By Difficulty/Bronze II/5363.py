for t in range(int(input())):
    s = input().split()
    ans = s[2:]+s[:2]
    print(*ans)
