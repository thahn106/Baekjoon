N = int(input())
while N:
    while N>9:
        N = sum(list(map(int,list(str(N)))))
    print(N)
    N = int(input())
