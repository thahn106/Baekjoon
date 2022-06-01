P, Q = map(int, input().split())
p, q = [], []
for i in range(1, max(P, Q)+1):
    if P % i == 0:
        p.append(i)
    if Q % i == 0:
        q.append(i)
for P in p:
    for Q in q:
        print(P, Q)
