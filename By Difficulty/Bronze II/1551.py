N,K = map(int,input().split())
a = list(map(int,input().split(',')))
for k in range(K):
    b = []
    for i in range(1,len(a)):
        b.append(a[i]-a[i-1])
    a = b
a = list(map(str,a))
print(",".join(a))
