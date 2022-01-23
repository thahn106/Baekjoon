for t in range(int(input())):
    a = list(map(int,input().split()))
    n = a[0]
    avg = sum(a[1:])/n
    ans = 0
    for i in a[1:]:
        if i>avg:
            ans +=1
    print("{:.3f}%".format(round(ans*100/n,3)))
