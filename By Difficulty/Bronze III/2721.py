T = [(i+1)*(i+2)//2 for i in range(301)]
for t in range(int(input())):
    ans = 0
    for i in range(1,int(input())+1):
        ans+=i*T[i]
    print(ans)
