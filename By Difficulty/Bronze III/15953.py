for t in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    if a:
        if a<=1:
            ans +=500
        elif a<=3:
            ans +=300
        elif a<=6:
            ans +=200
        elif a<=10:
            ans+=50
        elif a<=15:
            ans+=30
        elif a<=21:
            ans+=10
    if b:
        if b<=1:
            ans +=512
        elif b<=3:
            ans +=256
        elif b<=7:
            ans +=128
        elif b<=15:
            ans +=64
        elif b<=31:
            ans+=32
    print(ans*10000)
