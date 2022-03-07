sl = input().split()
while sl != ['#']:
    ans = []
    for c in sl:
        ans.append(c[::-1])
    print(*ans)
    sl = input().split()
