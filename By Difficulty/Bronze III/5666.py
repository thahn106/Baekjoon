try:
    while True:
        H,P = map(int,input().split())
        print("{:.2f}".format(H/P))
except EOFError as e:
    pass
