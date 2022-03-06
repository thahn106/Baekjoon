for t in range(int(input())):
    a,b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    ans = str(a+b)
    print(int(ans[::-1]))
