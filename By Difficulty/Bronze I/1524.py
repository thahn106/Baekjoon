for t in range(int(input())):
    _ = input()
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if max(A)>=max(B):
        print("S")
    else:
        print("B")
