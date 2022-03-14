N = int(input())
K = int(input())

valid = [0]*(N+1)

q = [1]
while q:
    cur = q.pop(0)
    valid[cur] = 1
    for k in range(2,K+1):
        if k*cur>N:
            break
        if not valid[k*cur]:
            valid[k*cur] = 1
            q.append(k*cur)
print(sum(valid))
