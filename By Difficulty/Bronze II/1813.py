t = int(input())
a = list(map(int,input().split()))
counts = [0 for i in range(51)]
for i in a:
    counts[i] +=1

ans = -1
for i in range(51):
    if counts[i]==i:
        ans = i
print(ans)
