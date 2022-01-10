A, B, V = map(int,input().split())
ans = (V-A)//(A-B)
if (ans)*(A-B)+A>=V:
    print(ans+1)
else:
    print(ans+2)
