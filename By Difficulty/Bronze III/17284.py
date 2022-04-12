ans = 5000
for i in list(map(int,input().split())):
    ans -= [0,500,800,1000][i]
print(ans)
