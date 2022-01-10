N = int(input())
if N == 4 or N == 7:
    print(-1)
else:
    ans = 0
    while N%5:
        ans +=1
        N -= 3
    ans += N//5
    print(ans)
