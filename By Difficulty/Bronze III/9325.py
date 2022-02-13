for t in range(int(input())):
    s = int(input())
    n = int(input())
    for i in range(n):
        q,p = map(int,input().split())
        s += q*p
    print(s)
