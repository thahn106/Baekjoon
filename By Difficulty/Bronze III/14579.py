a,b = map(int,input().split())
ans = 1
for i in range(a,b+1):
    ans = ans* ((i)*(i+1)//2)
    ans = ans % 14579

print(ans)
