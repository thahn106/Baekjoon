n = int(input())
while n>0:
    ans = 0
    cur = 0
    for i in range(n):
        s,t = map(int,input().split())
        ans += s*(t-cur)
        cur = t
    print("{} miles".format(ans))
    n = int(input())
