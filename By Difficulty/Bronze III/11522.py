for _ in range(int(input())):
    k, n = map(int, input().split())
    print(k, n*(n+1)//2, n*n, n*(n+1))
