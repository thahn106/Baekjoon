for t in range(int(input())):
    n = int(input())
    ans = "Pairs for {}:".format(n)
    for i in range(1, (n+1)//2):
        q = ""
        if i != 1:
            q += ","
        q += " {} {}".format(i,n-i)
        ans += q
    print(ans)
