n = int(input())
a = list(map(int,input().split()))
ans = []
for i,d in enumerate(a):
    ans.insert(i-d,i+1)
print(*ans)
