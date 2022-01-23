M = int(input())
N = int(input())
sq = []
for i in range(1,101):
    if M<=i*i<=N:
        sq.append(i*i)
if sq:
    print(sum(sq))
    print(sq[0])
else:
    print(-1)
