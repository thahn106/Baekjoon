A,B = map(int,input().split())
A,B = min(A,B), max(A,B)
print((B-A)*(B-A+1)//2 + (B-A+1)*A)
