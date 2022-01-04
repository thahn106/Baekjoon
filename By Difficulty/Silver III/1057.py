N, K, I = map(int,input().split())
ans =0
while not K == I:
    K = (K-1)//2+1
    I = (I-1)//2+1
    ans += 1
print(ans)
