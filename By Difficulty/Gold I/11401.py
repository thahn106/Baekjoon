N,K = map(int,input().split())
mod = 1000000007
num = N
K = min(K,N-K)
p = 1
q = 1

for i in range(K):
    p = p*(N-i) % mod
    q = q*(i+1) % mod
print(p*pow(q,-1,mod) % mod)
