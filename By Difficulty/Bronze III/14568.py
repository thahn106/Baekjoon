N = int(input())

ans = 0
for i in range(1,N-2):
    for j in range(1,N-1-i):
        k = N-i-j
        if k>0 and k%2==0 and i>=j+2:
            ans+=1
print(ans)
