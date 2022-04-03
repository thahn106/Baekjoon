N,K = map(int,input().split())
a = []
for i in range(1,K+1):
    a.append(int(str(N*i)[::-1]))
print(max(a))
