N = int(input())
while N:
    R = list(map(int,input().split()))
    J = sum(R)
    M = N-J
    print(f"Mary won {M} times and John won {J} times")
    N = int(input())
