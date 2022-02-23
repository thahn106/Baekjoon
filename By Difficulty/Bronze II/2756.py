for t in range(int(input())):
    s = list(map(float,input().split()))
    a = 0
    for i in range(3):
        x,y = s[2*i:2*i+2]
        d = x*x+y*y
        if d<=9:
            a+=100
        elif d<=36:
            a+=80
        elif d<=81:
            a+=60
        elif d<=144:
            a+=40
        elif d<=225:
            a+=20
    b = 0
    for i in range(3):
        x,y = s[2*i+6:2*i+8]
        d = x*x+y*y
        if d<=9:
            b+=100
        elif d<=36:
            b+=80
        elif d<=81:
            b+=60
        elif d<=144:
            b+=40
        elif d<=225:
            b+=20
    if a>b:
        r = "PLAYER 1 WINS."
    elif b>a:
        r = "PLAYER 2 WINS."
    else:
        r = "TIE."
    print(f"SCORE: {a} to {b}, {r}")
