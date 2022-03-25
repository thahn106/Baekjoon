for t in range(int(input())):
    N = sorted(list(map(int,input().split())))
    if N[3]-N[1]>=4:
        print("KIN")
    else:
        print(sum(N[1:4]))
