for t in range(int(input())):
    a = input().split()
    ans = []
    for i in a:
        ans.append(i[::-1])
    print(*ans)
