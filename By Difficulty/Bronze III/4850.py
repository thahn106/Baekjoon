try:
    while True:
        s = input()
        N,w,d,r = map(int,s.split())
        dif = (w*N*(N-1)//2 -r)//d
        if dif == 0:
            dif = N
        print(dif)
except EOFError as e:
    pass
