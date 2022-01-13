a = list(map(int,input().split()))
while a[0]:
    n = len(a)//2
    ans = 1
    for i in range(1,n+1):
        ans*=a[2*i-1]
        ans-=a[2*i]
    print(ans)
    a = list(map(int,input().split()))
