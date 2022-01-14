for t in range(int(input())):
    dict = {}
    for n in range(int(input())):
        a,b = input().split()
        if b in dict:
            dict[b]+=1
        else:
            dict[b]=2
    ans = 1
    for b in dict:
        ans*=(dict[b])
    print(ans-1)
