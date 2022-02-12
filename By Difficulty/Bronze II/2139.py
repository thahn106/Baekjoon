def leap(n):
    return n%4==0 and (n%400==0 or not(n%100==0))

months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
lmonths = [0,31,29,31,30,31,30,31,31,30,31,30,31]
d,m,y = map(int,input().split())
while d and m and y:
    ans = 0
    ma = months
    if leap(y):
        ma = lmonths
    for i in range(m):
        ans += ma[i]
    ans += d
    print(ans)
    d,m,y = map(int,input().split())
