n = input()
while n != '0':
    N,P = map(int,n.split())
    ans = []
    p1 = 4*((P+1)//2)-1-P
    ans.append(p1)
    P = N+1-P
    p1 = 4*((P+1)//2)-1-P
    ans.append(P)
    ans.append(p1)
    ans.sort()
    print(*ans)
    n = input()
