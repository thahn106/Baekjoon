import sys
input = sys.stdin.buffer.readline

N = int(input())
counts = [0 for i in range(8001)]
sum = 0
for i in range(N):
    n = int(input())
    sum += n
    counts[n+4000] += 1

print(round(sum/N))

run = 0
i = -1
while run < (N+1)//2:
    i+=1
    run+=counts[i]
print(i-4000)

m = max(counts)
maxs = []
for i in range(8001):
    if counts[i]==m:
        maxs.append(i-4000)
if len(maxs)>1:
    print(maxs[1])
else:
    print(maxs[0])

MAX = 4000
while not counts[MAX+4000]:
    MAX -= 1
MIN = -4000
while not counts[MIN+4000]:
    MIN += 1
print(MAX-MIN)
