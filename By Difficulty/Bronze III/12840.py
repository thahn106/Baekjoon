h,m,s = map(int,input().split())
t = 3600*h+60*m+s
for q in range(int(input())):
    s = input()
    if s == '3':
        h = t // 3600
        m =  (t//60) %60
        s =  t % 60
        print(h,m,s)
    else:
        a,c = map(int,s.split())
        if a == 1:
            t = (t+c) % (24*60*60)
        else:
            t = (t-c) % (24*60*60)
