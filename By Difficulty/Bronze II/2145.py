N = int(input())
while N:
    s = str(N)
    while len(s)>1:
        s =str(sum(list(map(int,list(s)))))
    print(s)
    N = int(input())
