a = list(map(int,input().split()))
while min(a) and max(a):
    ans = 0
    while min(a)!=max(a):
        a = [abs(a[(i+1)%4]-a[i]) for i in range(4)]
        ans += 1
    print(ans)
    a = list(map(int,input().split()))
