for i in range(3):
    ans = 1
    cur = 0
    temp=0
    for c in input():
        if c !=cur:
            cur = c
            temp = 1
        else:
            temp+=1
        ans = max(ans,temp)
    print(ans)
