for t in range(int(input())):
    a,b = map(int,input().split())
    ans = (b*(b+1))//2 -  ((a-1)*a)//2
    if t:
        print("")
    print(f"Scenario #{t+1}:")
    print(ans)
