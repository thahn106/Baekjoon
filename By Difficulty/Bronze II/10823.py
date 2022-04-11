import sys
ans = []
for line in sys.stdin:
    ans.append(line.strip())

ans = "".join(ans)
print(sum(list(map(int, ans.split(',')))))
