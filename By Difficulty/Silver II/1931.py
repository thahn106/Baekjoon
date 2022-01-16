import sys
input = sys.stdin.buffer.readline

N = int(input())
conf = []
for i in range(N):
    start, end = map(int,input().split())
    conf.append((end,start))

conf.sort()

ans = 0
end = 0

for e,s in conf:
    if s>=end:
        ans+=1
        end = e
print(ans)
