ans = [0,0,0]
s = list(range(3))
for i in range(int(input())):
    a,b,g = map(int,input().split())
    a -= 1
    b -= 1
    s[a],s[b] = s[b],s[a]
    ans[s[g-1]] += 1
print(max(ans))
