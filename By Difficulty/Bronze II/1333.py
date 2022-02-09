N,L,D = map(int,input().split())
cur = 0
while True:
    if cur%(L+5) >= L or cur >= (L+5)*N:
        print(cur)
        break
    cur += D
