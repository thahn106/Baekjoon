def count_ones(x):
    ones = 0
    for i in bin(x)[2:]:
        ones+= i=='1'
    return ones

N,K = map(int,input().split())

ans = 0
add = 1
while(count_ones(N)>K):
    if N%2:
        ans +=add
        N += 1
    N = N//2
    add*=2
print(ans)
