try:
    while True:
        n, s = map(int, input().split())
        print(s//(n+1))
except EOFError as e:
    pass
