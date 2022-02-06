N,M,K = map(int,input().split())
print(min(M,K)+min(N-K,N-M))
