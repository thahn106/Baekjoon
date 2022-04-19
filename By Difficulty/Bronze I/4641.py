s = list(map(int, input().split()))
while s[0] != -1:
    ans = -1
    for i in s:
        if 2*i in s:
            ans +=1
    print(ans)
    s = list(map(int, input().split()))
