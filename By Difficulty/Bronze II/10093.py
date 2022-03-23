A,B = map(int,input().split())
A,B = min(A,B), max(A,B)
print(max(0,B-A-1))
print(*list(range(A+1,B)))
