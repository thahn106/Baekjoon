N = int(input())
a = {}
for i in range(N):
    s = input()
    if s in a:
        a[s]+=1
    else:
        a[s]=1

ans = []
m = max(a.values())
# print(f"{m=}")
for c in a:
    if a[c] == m:
        ans.append(c)
ans.sort()
print(ans[0])
