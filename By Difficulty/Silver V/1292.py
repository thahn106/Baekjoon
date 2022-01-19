ans = []
for i in range(45):
    ans+=[i+1]*(i+1)

A,B = map(int,input().split())
s = 0
for j in range(A,B+1):
    s += ans[j-1]

print(s)
