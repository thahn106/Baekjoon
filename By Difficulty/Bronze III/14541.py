n = int(input())
while n != -1:
    ans = 0
    T = 0
    for i in range(n):
        s, t = map(int, input().split())
        ans += s*(t-T)
        T = t
    print(f'{ans} miles')
    n = int(input())
