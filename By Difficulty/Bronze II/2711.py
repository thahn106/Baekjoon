for i in range(int(input())):
    n,s = input().split()
    s=list(s)
    s.pop(int(n)-1)
    print("".join(s))
