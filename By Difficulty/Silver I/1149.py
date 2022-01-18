N = int(input())
r = list(map(int,input().split()))
for n in range(1,N):
    nc = list(map(int,input().split()))
    r = [nc[0]+min(r[1],r[2]),nc[1]+min(r[0],r[2]),nc[2]+min(r[1],r[0])]
print(min(r))
