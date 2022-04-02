for t in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    print(2*(max(x)-min(x)))
