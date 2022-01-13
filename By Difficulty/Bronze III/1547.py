ans = [0,1,0,0]
for m in range(int(input())):
    a,b = map(int,input().split())
    ans[a],ans[b] = ans[b],ans[a]

print(ans.index(1))
