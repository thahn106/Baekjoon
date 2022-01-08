A,B = input().split()
a,b = len(A),len(B)
ans = b
for i in range(b-a+1):
    t = 0
    for j in range(a):
        if A[j]!=B[i+j]:
            t+=1
    ans = min(ans,t)
print(ans)
