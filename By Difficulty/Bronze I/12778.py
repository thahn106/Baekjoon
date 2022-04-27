for t in range(int(input())):
    M, c = input().split()
    ans = []
    if c == 'N':
        a = list(map(int, input().split()))
        for i in a:
            ans.append(chr(i+64))
        print(*ans)
    else:
        a = input().split()
        for i in a:
            ans.append(ord(i)-64)
        print(*ans)
