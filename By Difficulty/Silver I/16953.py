A,B = map(int,input().split())

ans = 1
while B>A:
    if B%10==1:
        ans += 1
        B = (B-1)//10
    elif B%2==0:
        ans +=1
        B = B//2
    else:
        B = -1


if A == B:
    print(ans)
else:
    print(-1)
