N = int(input())
friends = []
for i in range(N):
    s = input()
    f = []
    for c in range(N):
        if s[c] == "Y":
            f.append(c)
    friends.append(f)
ans =0
for p in friends:
    cur = []+p
    for f in p:
        cur += friends[f]
    cur = set(cur)
    ans = max(ans, len(cur)-1)
print(ans)
