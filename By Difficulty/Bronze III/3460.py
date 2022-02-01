for t in range(int(input())):
    n = int(input())
    s = bin(n)[2:][::-1]
    ans = []
    for i in range(len(s)):
        if s[i]=="1":
            ans.append(i)
    print(*ans)
