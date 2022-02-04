a = list(map(int,input().split()))
while not (min(a)==0 and max(a) == 0):
    ans = (sum(a)-min(a)-max(a))/4
    if int(ans)==ans:
        ans = int(ans)
    print(ans)
    a = list(map(int,input().split()))
