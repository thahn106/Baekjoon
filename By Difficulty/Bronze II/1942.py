for i in range(3):
    S,E = input().split()
    SH, SM, SS = map(int, S.split(":"))
    EH, EM, ES = map(int, E.split(":"))
    s = SH*60*60+SM*60+SS
    e = EH*60*60+EM*60+ES
    i = s
    ans = 0
    while True:
        H,t = divmod(i,3600)
        M,S = divmod(t,60)
        ti = H*10000+M*100+S
        if ti%3==0:
            ans +=1
        if i == e:
            break
        i = (i+1)%(24*60*60)
    print(ans)
