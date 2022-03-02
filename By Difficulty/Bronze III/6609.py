try:
    while True:
        M, P, L, E, R, S, N = map(int,input().split())
        for i in range(N):
            ne = E*M
            M = P//S
            P = L//R
            L = ne
        print(M)

except EOFError as e:
    pass
