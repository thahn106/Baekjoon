X = int(input())
N = int(input())
a = [int(input()) for i in range(N)]
print(X*(N+1)-sum(a))
