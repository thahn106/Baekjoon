for t in range(int(input())):
    a,b = map(int,input().split())
    a = a%10
    b = (b%4)+4
    ans = (a**b)%10
    if ans == 0:
        ans = 10
    print(ans)
