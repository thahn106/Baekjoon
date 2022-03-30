q = []
for i in range(1,9):
    n = int(input())
    q.append((n,i))

q.sort()
ans = 0
ansq = []
for n,i in q[-5:]:
    ans += n
    ansq.append(i)

ansq.sort()
print(ans)
print(*ansq)
