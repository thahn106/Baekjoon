N = int(input())
people = []
for i in range(N):
    a,b = map(int,input().split())
    people.append((a,b))

ans = []
for i in range(N):
    t = 1
    a,b = people[i]
    for j in range(N):
        c,d = people[j]
        if c>a and d>b:
            t +=1
    ans.append(t)
print(*ans)
